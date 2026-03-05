# 🎬 Django Movie Ticket Booking System

A simple **Movie Ticket Booking Web Application** built with **Python and Django**.
Users can register, login, view movies, and book tickets online.

---

## 🚀 Features

- User Registration and Login
- View Available Movies
- Book Movie Tickets
- Seat Availability Check
- View My Bookings
- Cancel Booking
- Admin Panel for Movie Management

---

## 🛠️ Technologies Used

- Python
- Django
- PostgreSQL / SQLite
- HTML
- CSS
- Bootstrap

---

## 📂 Project Structure

```
django_ticketbook/
│
├── movies/          # Movie management app
├── bookings/        # Ticket booking app
├── templates/       # HTML templates
├── static/          # CSS / JS / Images
├── manage.py
└── requirements.txt
```

---

## ⚙️ Installation

1️⃣ Clone the repository

```
git clone https://github.com/hemangiram/movie_ticketbook.git
```

2️⃣ Go to project directory

```
cd django_ticketbook
```

3️⃣ Create virtual environment

```
python -m venv venv
```

4️⃣ Activate virtual environment

Linux / Mac

```
source venv/bin/activate
```

5️⃣ Install dependencies

```
pip install -r requirements.txt
```

6️⃣ Apply migrations

```
python manage.py makemigrations
python manage.py migrate
```

7️⃣ Run the server

```
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000
```

---

## 👤 Admin Access

Create admin user:

```
python manage.py createsuperuser
```

Open admin panel:

```
http://127.0.0.1:8000/admin
```

---

- Movie List Page
- Ticket Booking Page
- My Bookings Page
- Admin Dashboard

## 📌 Future Improvements

- Seat Selection UI

---
