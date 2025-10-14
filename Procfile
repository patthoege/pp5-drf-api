web: python manage.py collectstatic --noinput && gunicorn pp5_drf_api.wsgi
release: python manage.py makemigrations && python manage.py migrate