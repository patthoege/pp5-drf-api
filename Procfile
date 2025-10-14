release: python manage.py migrate
web: python manage.py collectstatic --noinput && gunicorn pp5_drf_api.wsgi