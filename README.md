# Little Lemon Web Application API

Django REST Framework project for the Little Lemon restaurant capstone. Includes a responsive landing page, menu API, table-booking API, registration/token authentication, Django admin, and automated unit tests.

## Features
- **Menu API**: Browse and manage menu items (`/api/menu/`).
- **Table Booking API**: Reserve tables and inspect reservations (`/api/bookings/`).
- **User Authentication**: User registration (`/api/registration/`) and DRF token-based auth (`/api/token/login/`, `/api/token/logout/`).
- **Static Frontend**: Static templates and assets for the Little Lemon web page.
- **Automated Tests**: Unit tests covering views, models, and API endpoints.

---

## Getting Started

### 1. Prerequisites
- Python 3.10+
- Git

### 2. Setup Virtual Environment
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Migrations
SQLite is configured by default for easy local development.
```bash
python manage.py makemigrations restaurant
python manage.py migrate
```
*(Optional: To use MySQL, set `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, and `DB_PORT` in your environment before migrating).*

### 5. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 6. Run Development Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

---

## API Endpoints

| Endpoint | Method | Description | Auth Required |
|---|---|---|---|
| `/api/menu/` | GET | List all menu items | No |
| `/api/menu/` | POST | Create menu item | Yes (Token) |
| `/api/menu/<id>/` | GET, PUT, PATCH, DELETE | Retrieve, update or delete a menu item | Yes (Token for write) |
| `/api/bookings/` | GET, POST | List bookings or create a new booking | Yes (Token) |
| `/api/bookings/<id>/` | GET, PUT, PATCH, DELETE | Manage individual booking | Yes (Token) |
| `/api/registration/` | POST | Register a new user (`username`, `password`) | No |
| `/api/token/login/` | POST | Obtain DRF Auth Token | No |
| `/api/token/logout/` | POST | Invalidate current Auth Token | Yes (Token) |

---

## Testing & API Client Setup (Insomnia / Postman)

### Running Automated Tests
```bash
python manage.py test
```

### Insomnia / Postman Example
1. Register a new user at `POST /api/registration/`:
   ```json
   {
     "username": "lemonuser",
     "password": "StrongPass123"
   }
   ```
2. Obtain authentication token at `POST /api/token/login/` using the credentials above.
3. Set the header for protected requests:
   ```http
   Authorization: Token <YOUR_AUTH_TOKEN>
   ```
