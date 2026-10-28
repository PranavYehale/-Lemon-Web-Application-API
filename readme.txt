# Little Lemon Web Application API

Django REST Framework project for the Little Lemon restaurant capstone. Includes a home page, menu API, table-booking API, registration/token authentication, admin, and tests.

## Run locally
1. Install Python 3.10+.
2. Create and activate a virtual environment.
3. Run `pip install -r requirements.txt`.
4. Run `python manage.py makemigrations restaurant`.
5. Run `python manage.py migrate`.
6. Run `python manage.py createsuperuser` (optional).
7. Run `python manage.py runserver`.
8. Open http://127.0.0.1:8000/.

SQLite is used for local setup by default. To use MySQL, create a database and set DB_NAME, DB_USER, DB_PASSWORD, DB_HOST and DB_PORT environment variables before running migrations.

## API routes
- GET /api/menu/ — list menu items; POST requires authentication.
- /api/menu/<id>/ — retrieve/update/delete menu item.
- /api/bookings/ — booking list/create (authentication required).
- /api/bookings/<id>/ — retrieve/update/delete booking (authentication required).
- POST /api/registration/ — create a user with username/password.
- POST /api/token/login/ — obtain DRF token.
- POST /api/token/logout/ — delete current token.

## Test
`python manage.py test`

## Insomnia
Register at `/api/registration/` with JSON `{"username":"lemonuser","password":"StrongPass123"}`. POST username/password to `/api/token/login/`, then use `Authorization: Token YOUR_TOKEN` for protected endpoints.

Do not commit production passwords, tokens, or secret keys. This is a starter implementation based on the visible rubric; test it in your environment before submitting.
