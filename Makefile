build:
	docker-compose build

migrations:
	docker-compose run --rm app sh -c "python manage.py makemigrations core"

test:
	docker-compose run --rm app sh -c "python manage.py test"

test-flake: test
	docker-compose run --rm app sh -c "flake8"
