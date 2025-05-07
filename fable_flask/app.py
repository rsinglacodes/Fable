from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import random
from transformers import pipeline
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import io
import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": ["http://localhost:8000", "http://127.0.0.1:8000"]}})

# Initialize emotion classifier
emotion_classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion", top_k=1)

# Mood mapping
MOOD_MAP = {
    "joy": "excited",
    "love": "happy",
    "anger": "annoyed",
    "fear": "anxious",
    "sadness": "sad",
    "surprise": "surprised",
    # Fallback for neutral or unclear cases
    "neutral": "calm"
}

# Simulated distance calculation (in miles)
def calculate_distance(origin_city, destination_city):
    return random.randint(100, 2000)

def estimate_trip_cost(data):
    try:
        origin_city = data.get('origin_city')
        destination_city = data.get('destination_city')
        travel_days = int(data.get('travel_days'))
        num_guests = int(data.get('num_guests'))
        accommodation_type = data.get('accommodation_type')

        if not all([origin_city, destination_city, travel_days, num_guests, accommodation_type]):
            return {"error": "All fields are required"}, 400
        if travel_days < 1 or travel_days > 30:
            return {"error": "Travel days must be between 1 and 30"}, 400
        if num_guests < 1 or num_guests > 10:
            return {"error": "Number of guests must be between 1 and 10"}, 400
        if accommodation_type not in ['budget', 'standard', 'luxury']:
            return {"error": "Invalid accommodation type"}, 400

        distance = calculate_distance(origin_city, destination_city)
        if distance < 500:
            travel_cost = 8300 * num_guests
        elif distance < 1000:
            travel_cost = 16600 * num_guests
        else:
            travel_cost = 24900 * num_guests

        if accommodation_type == 'budget':
            hotel_cost = 4150 * travel_days * num_guests
        elif accommodation_type == 'standard':
            hotel_cost = 8300 * travel_days * num_guests
        else:
            hotel_cost = 16600 * travel_days * num_guests

        food_cost = 2490 * num_guests * travel_days
        total_cost = travel_cost + hotel_cost + food_cost

        return {
            'travel_cost': round(travel_cost, 2),
            'hotel_cost': round(hotel_cost, 2),
            'food_cost': round(food_cost, 2),
            'total_cost': round(total_cost, 2)
        }, 200

    except ValueError:
        return {"error": "Invalid numeric input"}, 400
    except Exception as e:
        logger.error(f"Error in estimate_trip_cost: {str(e)}")
        return {"error": f"Server error: {str(e)}"}, 500

@app.route('/api/trip-cost/', methods=['POST'])
def trip_cost():
    data = request.get_json()
    result, status_code = estimate_trip_cost(data)
    return jsonify(result), status_code

analyzer = SentimentIntensityAnalyzer()

@app.route('/api/analyze-review/', methods=['POST'])
def analyze_review():
    try:
        data = request.get_json()
        review_text = data.get('review', '')
        
        if not review_text:
            return jsonify({'error': 'No review text provided'}), 400
            
        scores = analyzer.polarity_scores(review_text)
        compound_score = scores['compound']
        
        if compound_score >= 0.05:
            sentiment = 'positive'
        elif compound_score <= -0.05:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
            
        return jsonify({
            'sentiment': sentiment,
            'score': compound_score
        }), 200
        
    except Exception as e:
        logger.error(f"Error in analyze_review: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/detect-mood/', methods=['POST'])
def detect_mood():
    try:
        data = request.get_json()
        review_text = data.get('review', '')
        
        if not review_text:
            return jsonify({'error': 'No review text provided'}), 400
            
        emotion_result = emotion_classifier(review_text)
        top_emotion = emotion_result[0][0]['label']
        mood = MOOD_MAP.get(top_emotion, 'neutral')
        
        logger.debug(f"Detected mood: {mood}")
        return jsonify({
            'mood': mood,
            'emotion': top_emotion
        }), 200
        
    except Exception as e:
        logger.error(f"Error in detect_mood: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/invoice/', methods=['POST'])
def generate_invoice():
    try:
        data = request.get_json()
        logger.debug(f"Received invoice data: {data}")
        
        required_fields = ['booking_id', 'hotel_name', 'user_name', 'user_email', 
                         'check_in', 'check_out', 'guests', 'total_price', 'location']
        if not all(field in data for field in required_fields):
            missing = [field for field in required_fields if field not in data]
            logger.error(f"Missing fields: {missing}")
            return jsonify({'error': f'Missing required fields: {missing}'}), 400
            
        # Validate data types
        try:
            data['guests'] = int(data['guests'])
            data['total_price'] = float(data['total_price'])
        except (ValueError, TypeError) as e:
            logger.error(f"Invalid data types: {str(e)}")
            return jsonify({'error': 'Invalid data types for guests or total_price'}), 400

        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        elements = []
        
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            'Title',
            parent=styles['Heading1'],
            fontSize=18,
            spaceAfter=20,
            textColor=colors.darkblue
        )
        normal_style = ParagraphStyle(
            'Normal',
            parent=styles['Normal'],
            fontSize=12,
            spaceAfter=10
        )
        
        elements.append(Paragraph("Hotel Booking Invoice", title_style))
        elements.append(Paragraph(f"Invoice #{data['booking_id']}", normal_style))
        elements.append(Paragraph(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d')}", normal_style))
        elements.append(Spacer(1, 0.25*inch))
        
        elements.append(Paragraph("Guest Information", styles['Heading2']))
        guest_info = [
            f"Name: {data['user_name']}",
            f"Email: {data['user_email']}"
        ]
        for info in guest_info:
            elements.append(Paragraph(info, normal_style))
        elements.append(Spacer(1, 0.25*inch))
        
        elements.append(Paragraph("Booking Details", styles['Heading2']))
        booking_info = [
            f"Hotel: {data['hotel_name']}",
            f"Location: {data['location']}",
            f"Check-in: {data['check_in']}",
            f"Check-out: {data['check_out']}",
            f"Guests: {data['guests']}"
        ]
        for info in booking_info:
            elements.append(Paragraph(info, normal_style))
        elements.append(Spacer(1, 0.25*inch))
        
        elements.append(Paragraph("Price Details", styles['Heading2']))
        price_data = [
            ["Description", "Amount (INR)"],
            ["Room Charges", f"₹{data['total_price']:.2f}"]
        ]
        price_table = Table(price_data)
        price_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        elements.append(price_table)
        
        elements.append(Spacer(1, 0.25*inch))
        elements.append(Paragraph(f"Total: ₹{data['total_price']:.2f}", ParagraphStyle(
            'Total',
            parent=styles['Normal'],
            fontSize=14,
            fontName='Helvetica-Bold',
            spaceBefore=10
        )))
        
        doc.build(elements)
        buffer.seek(0)
        
        return send_file(
            buffer,
            as_attachment=True,
            download_name=f"invoice_{data['booking_id']}.pdf",
            mimetype='application/pdf'
        )
        
    except Exception as e:
        logger.error(f"Error in generate_invoice: {str(e)}")
        return jsonify({'error': f"Server error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)