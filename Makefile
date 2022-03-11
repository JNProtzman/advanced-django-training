test:
	docker-compose run app sh -c "python manage.py test"

test-flake:
	docker-compose run app sh -c "python manage.py test && flake8"

build:
	docker-compose build

migrations:
	docker-compose run app sh -c "python manage.py makemigrations core"
