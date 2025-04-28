HEAD
# Fable - Online Hotel Booking Application

Fable is a modern, elegant online hotel booking web application developed using Django. It allows users to browse, book, and manage hotel stays seamlessly.

The backend is powered by Django, and the project is structured into three main Django apps:
- **AuthApp**: Handles user authentication (login, registration, logout).
- **MainApp**: Manages homepage, general pages, and common functionalities.
- **HotelApp**: Manages hotel listings, hotel details, and booking logic.

The core Django project is contained inside the **FableProject** directory.

---

## Features
- User Registration and Login
- Hotel Browsing and Booking
- Booking Management
- Clean and Modern UI (inspired by Airbnb)

---

## Getting Started

Follow these steps to set up the project locally.

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/fable.git
cd fable
```

### 2. Create and Activate a Virtual Environment

#### Windows
```bash
python -m venv env
env\Scripts\activate
```

#### macOS/Linux
```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install the Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Development Server
```bash
python manage.py runserver
```

The application will start running at `http://127.0.0.1:8000/`

---

## Project Structure
```
FableProject/       # Main Django project settings and configuration
AuthApp/            # Handles authentication (login, signup, logout)
MainApp/            # Core pages like Home, About, etc.
HotelApp/           # Hotel listings, details, and bookings
manage.py           # Django management script
requirements.txt    # Python dependencies
```

---

## Notes
- Make sure you have Python 3.8 or higher installed.
- Don't forget to set up the database and superuser if you want to access the Django admin panel.

To create a superuser:
```bash
python manage.py createsuperuser
```

---

## License
This project is for educational purposes and personal use.

---

## Author
Developed by [Your Name]

---

Enjoy booking hotels with Fable! ✨


# Fable
76970162b7aa6975572f889b389ec50d8363bdd0
