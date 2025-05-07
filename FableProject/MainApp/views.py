from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
import random
import requests
import json
from .forms import FeedbackForm
from .models import Feedback

def home(request):
    return render(request, 'index.html')

def term(request):
    return render(request, 'terms.html')

def setting(request):
    return render(request, 'setting.html')

def help(request):
    return render(request, 'help.html')

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            comment = form.cleaned_data['comment']
            
            # Send comment to Flask API for sentiment analysis
            try:
                sentiment_response = requests.post(
                    'http://localhost:5000/api/analyze-review/', 
                    json={'review': comment},
                    timeout=5
                )
                if sentiment_response.status_code == 200:
                    sentiment_data = sentiment_response.json()
                    feedback.sentiment = sentiment_data['sentiment']
                else:
                    feedback.sentiment = 'unknown'
                    messages.warning(request, 'Sentiment analysis failed. Feedback saved without sentiment.')
            except requests.RequestException as e:
                feedback.sentiment = 'unknown'
                messages.warning(request, 'Sentiment analysis service unavailable. Feedback saved without sentiment.')
            
            # Send comment to Flask API for mood detection
            try:
                mood_response = requests.post(
                    'http://localhost:5000/api/detect-mood/', 
                    json={'review': comment},
                    timeout=5
                )
                if mood_response.status_code == 200:
                    mood_data = mood_response.json()
                    feedback.mood = mood_data['mood']
                else:
                    feedback.mood = 'unknown'
                    messages.warning(request, 'Mood detection failed. Feedback saved without mood.')
            except requests.RequestException as e:
                feedback.mood = 'unknown'
                messages.warning(request, 'Mood detection service unavailable. Feedback saved without mood.')
            
            feedback.save()
            messages.success(request, 'Thank you for your feedback!')
            return redirect('thanks', sentiment=feedback.sentiment)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})

def contact(request):
    return render(request, 'contact.html')

def thanks(request, sentiment=None):
    mood = None
    
    if sentiment:
        try:
            latest_feedback = Feedback.objects.filter(sentiment=sentiment).order_by('-created_at').first()
            if latest_feedback:
                mood = latest_feedback.mood
        except Exception:
            pass
    
    return render(request, 'thanks.html', {
        'sentiment': sentiment,
        'mood': mood
    })

def about(request):
    return render(request, 'about.html')

def beach(request):
    return render(request, 'beach.html')

def coming(request):
    return render(request, 'coming.html')

def confirm(request):
    return render(request, 'confirm.html')

def data(request):
    return render(request, 'data.html')

def homepage(request):
    return render(request, 'homepage.html')

def luxury(request):
    return render(request, 'luxury.html')

def learn(request):
    return render(request, 'learn.html')

def rooms(request):
    return render(request, 'rooms.html')

def search(request):
    return render(request, 'search.html')

def cost_estimator(request):
    return render(request, 'cost_estimator.html')

def trip_cost_estimate_api(request):
    if request.method == 'POST':
        try:
            # Parse JSON body
            data = json.loads(request.body.decode('utf-8'))

            # Extract required fields
            required_fields = ['origin_city', 'destination_city', 'travel_days', 'num_guests', 'accommodation_type']
            if not all(data.get(field) for field in required_fields):
                return JsonResponse({'error': 'All fields are required'}, status=400)

            # Send request to Flask API
            response = requests.post(
                'http://localhost:5000/api/trip-cost/',
                json=data,
                timeout=5
            )

            # Check Flask API response
            if response.status_code == 200:
                return JsonResponse(response.json(), status=200)
            else:
                print(f"Flask API error: {response.status_code} - {response.text}")
                return JsonResponse(
                    {'error': f'Failed to calculate estimate: {response.text}'},
                    status=response.status_code
                )

        except json.JSONDecodeError:
            print("JSON decode error: Invalid JSON format")
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        except requests.RequestException as e:
            print(f"Request exception: {str(e)}")
            return JsonResponse({'error': f'API service unavailable: {str(e)}'}, status=500)
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            return JsonResponse({'error': f'Server error: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

def generate_invoice(request):
    if request.method == 'POST':
        try:
            # Parse JSON body
            data = json.loads(request.body.decode('utf-8'))
            required_fields = ['booking_id', 'hotel_name', 'user_name', 'user_email', 
                             'check_in', 'check_out', 'guests', 'total_price', 'location']
            if not all(data.get(field) for field in required_fields):
                missing = [field for field in required_fields if field not in data]
                return JsonResponse({'error': f'Missing required fields: {missing}'}, status=400)

            # Send request to Flask API
            response = requests.post(
                'http://localhost:5000/api/invoice/',
                json=data,
                timeout=5
            )

            # Check Flask API response
            if response.status_code == 200:
                # Stream the PDF response
                response_content = response.content
                booking_id = data.get('booking_id', 'unknown')
                http_response = HttpResponse(
                    content=response_content,
                    content_type='application/pdf'
                )
                http_response['Content-Disposition'] = f'attachment; filename="invoice_{booking_id}.pdf"'
                return http_response
            else:
                print(f"Flask API error: {response.status_code} - {response.text}")
                return JsonResponse(
                    {'error': f'Failed to generate invoice: {response.text}'},
                    status=response.status_code
                )

        except json.JSONDecodeError:
            print("JSON decode error: Invalid JSON format")
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        except requests.RequestException as e:
            print(f"Request exception: {str(e)}")
            return JsonResponse({'error': f'API service unavailable: {str(e)}'}, status=500)
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            return JsonResponse({'error': f'Server error: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)