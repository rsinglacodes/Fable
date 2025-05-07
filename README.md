# Fable - Online Hotel Booking Application

Fable is a modern, elegant online hotel booking web application developed using **Django**, with additional smart features powered by a **Flask API**. It allows users to browse, book, and manage hotel stays, while also offering intelligent tools such as sentiment analysis, emotion detection, cost estimation, and PDF invoice generation.

---

## 🧩 Tech Stack
- **Frontend**: HTML, CSS, JS (Airbnb-inspired UI)
- **Backend**: Django + Flask
- **ML/NLP**: VADER, DistilBERT, ReportLab

---

## 🎯 Features
- User Registration and Login
- Hotel Browsing and Booking
- Booking Management
- Clean and Modern UI
- Smart Features via Flask API:
  - Feedback Sentiment Analysis
  - Mood Detection
  - Trip Cost Estimation
  - Invoice PDF Generation

---

## 🚀 Getting Started

### 🔹 Clone the Repository
```bash
git clone https://github.com/rsinglacodes/fable.git
cd fable
````

---

### 🔹 Run the Django Project

#### 1. Create and Activate a Virtual Environment

**Windows:**

```bash
python -m venv env
env\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv env
source env/bin/activate
```

#### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 3. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 4. Run Django Server

```bash
python manage.py runserver
```

The Django app will run at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### 🔹 Run the Flask API

The Flask API is located in the `fable_flask/` directory.

#### 1. Navigate to Flask Folder

```bash
cd fable_flask
```

#### 2. Install Flask-Specific Dependencies

```bash
pip install -r requirements.txt
```

#### 3. Run Flask Server

```bash
python app.py
```

The Flask API will run at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📡 Flask API Endpoints

### ✅ 1. Feedback Sentiment Analysis

* **Endpoint:** `/api/analyze-review/`
* **Request (JSON):**

  ```json
  { "review": "The hotel was amazing and the staff were kind!" }
  ```
* **Response (JSON):**

  ```json
  { "sentiment": "positive", "score": 0.84 }
  ```
* **Model:** VADER (lexicon-based sentiment analysis)

---

### ✅ 2. Mood Detection

* **Endpoint:** `/api/detect-mood/`
* **Request (JSON):**

  ```json
  { "review": "I'm feeling really happy with the service!" }
  ```
* **Response (JSON):**

  ```json
  { "mood": "happy", "emotion": "joy" }
  ```
* **Model:** DistilBERT via Hugging Face (`bhadresh-savani/distilbert-base-uncased-emotion`)

---

### ✅ 3. Trip Cost Estimator

* **Endpoint:** `/api/trip-cost/`
* **Request (JSON):**

  ```json
  {
    "origin_city": "Delhi",
    "destination_city": "Manali",
    "travel_days": 3,
    "num_guests": 2,
    "accommodation_type": "standard"
  }
  ```
* **Response (JSON):**

  ```json
  {
    "travel_cost": 16600,
    "hotel_cost": 83000,
    "food_cost": 12450,
    "total_cost": 112050
  }
  ```
* **Logic:** Rule-based cost calculator (demo)

---

### ✅ 4. Invoice Generator

* **Endpoint:** `/api/invoice/`
* **Request (JSON):**

  ```json
  {
    "booking_id": "BK1234",
    "hotel_name": "The Grand",
    "user_name": "John Doe",
    "user_email": "john@example.com",
    "check_in": "2025-06-01",
    "check_out": "2025-06-03",
    "guests": 2,
    "total_price": 15000,
    "location": "Manali"
  }
  ```
* **Response:** Downloads a **PDF Invoice**
* **Library Used:** `ReportLab`

---

## 🗂 Project Structure

```
FableProject/       # Main Django project settings and apps
AuthApp/            # Authentication logic
MainApp/            # Static/home pages
HotelApp/           # Hotel and booking logic
fable_flask/        # Flask ML & utility microservices
  └── app.py        # Main Flask API script
manage.py           # Django command-line utility
requirements.txt    # Dependencies
```

---

## 🛠 Notes

* Use Python 3.8 or higher.
* Run both servers in separate terminals for full functionality.
* To create Django superuser:

```bash
python manage.py createsuperuser
```

---

## 👨‍💻 Author

Developed by \[Your Name]

---

Enjoy booking smart with **Fable** ✨

