# JobTracker

A clean, dark-themed Django web application for tracking your personal job applications throughout the hiring process.

## Features

- **User authentication** — each user sees only their own applications
- **Full CRUD** — add, edit, and delete job applications
- **Inline status updates** — move applications through stages directly from the dashboard
- **Status filtering** — filter your list by Wishlist, Applied, Interview, Offer, or Rejected
- **CSV export** — download all your applications as a spreadsheet-ready CSV file
- **Favicon + custom logo** — polished UI with no external image dependencies

## Tech Stack

- Python 3.14 / Django 5.2 LTS
- SQLite (built-in, zero config)
- Tailwind CSS (CDN)
- Django built-in authentication

## Project Structure

```
jobtracker/
├── manage.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── applications/
    ├── models.py
    ├── views.py
    ├── forms.py
    ├── urls.py
    └── templates/
        ├── applications/
        └── registration/
```

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### ⚠️ Python 3.13+ Note (Windows)

There is a known bug with `venv` and `ensurepip` on Python 3.13+ on Windows. Create your virtual environment like this:

```bash
python -m venv venv --without-pip
venv\Scripts\Activate.ps1
python -m ensurepip --upgrade
```

This installs pip correctly inside the venv. Everything works normally after this step.

### Installation

1. Clone the repository:
```bash
   git clone <repo-url>
   cd jobtracker
```

2. Create and activate a virtual environment:
```bash
   python -m venv venv
   venv\Scripts\Activate.ps1   # Windows (PowerShell)
   source venv/bin/activate     # macOS/Linux
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

4. Apply migrations:
```bash
   python manage.py migrate
```

5. Create a superuser:
```bash
   python manage.py createsuperuser
```

6. Run the development server:
```bash
   python manage.py runserver
```

7. Open your browser at `http://127.0.0.1:8000/`

## Usage

- Log in with your superuser credentials
- Add applications with company, role, location, status, applied date, job URL, and notes
- Update the status of any application with one click from the dashboard
- Filter applications by status using the pills at the top
- Export all your applications to CSV from the navbar

## Job Application Statuses

| Status    | Description                        |
|-----------|------------------------------------|
| Wishlist  | Jobs you want to apply to          |
| Applied   | Application submitted              |
| Interview | Interview stage                    |
| Offer     | Offer received                     |
| Rejected  | Application unsuccessful           |

## Planned Features

- **Google Sheets import** — pull existing applications directly from a Google Sheet (model field already stubbed: `sheet_row_id`)
- **User registration page** — currently superuser-only login
- **Email reminders** — follow-up nudges for stale applications

## Deployment

This project is configured for deployment on [Railway](https://railway.app):

- `Procfile` — runs gunicorn
- `runtime.txt` — specifies Python version
- `whitenoise` — serves static files in production

See the deployment section in the docs for full instructions.

## License

MIT