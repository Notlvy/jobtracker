set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.filter(username='ivyadmins').exists() or User.objects.create_superuser('ivyadmin', 'szekely.timea@gmail.com', '3463')" | python manage.py shell