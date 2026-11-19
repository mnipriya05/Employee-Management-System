# Employee Management System

A web-based Employee Management System developed using Python and Django. This project allows users to manage employee records through a simple and user-friendly interface.

## Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML, CSS
- **Database:** SQLite
- **Tools:** VS Code, Git, GitHub

## Features

- Add new employee records.
- View all employee details.
- Update existing employee information.
- Delete employee records.
- Move deleted employees to the Trash section.
- View deleted employee records.
- Separate Home, Trash, About and Contact pages.

## Employee Details

The system manages the following employee information:

- Name
- Email
- Mobile Number
- Designation
- Department

## Project Structure

```text
django_mock/
│
└── config/
    ├── base/
    │   ├── migrations/
    │   ├── static/
    │   │   └── css/
    │   │       └── style.css
    │   ├── templates/
    │   │   ├── main.html
    │   │   ├── nav.html
    │   │   ├── home.html
    │   │   ├── update.html
    │   │   ├── trash.html
    │   │   ├── about.html
    │   │   └── contact.html
    │   ├── models.py
    │   ├── views.py
    │   └── urls.py
    │
    ├── config/
    ├── manage.py
    └── db.sqlite3
```

## Installation and Setup

1. Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

2. Navigate to the project directory:

```bash
cd django_mock/config
```

3. Create and activate a virtual environment:

```bash
python -m venv venv
```

4. Install Django:

```bash
pip install django==3.2.25
```

5. Apply database migrations:

```bash
python manage.py migrate
```

6. Start the development server:

```bash
python manage.py runserver
```

7. Open your browser:

```text
http://127.0.0.1:8000/
```

## Future Improvements

- User authentication and authorization.
- Employee search and filtering.
- Improved dashboard and user experience.

## Author

**Priya**

