makemigrations:
	DJANGO_SETTINGS_MODULE=shapely.settings.local python manage.py makemigrations

migrate:
	DJANGO_SETTINGS_MODULE=shapely.settings.local python manage.py migrate

start:
	DJANGO_SETTINGS_MODULE=shapely.settings.local python manage.py runserver 8000

shell:
	DJANGO_SETTINGS_MODULE=shapely.settings.local python manage.py shell_plus

test:
	DJANGO_SETTINGS_MODULE=shapely.settings.testing python manage.py test
