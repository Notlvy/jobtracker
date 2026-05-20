set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py shell -c "
from django.contrib.auth.models import User
import os
username = os.environ.get('ADMIN_USER', 'ivyadmin')
password = os.environ.get('ADMIN_PASSWORD', '')
email = os.environ.get('ADMIN_EMAIL', '')
if password and not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print('Superuser created!')
else:
    print('Superuser already exists or no password set.')
