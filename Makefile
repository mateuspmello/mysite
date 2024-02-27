build:
	docker-compose build

run: build
	docker-compose up

cleanup:
	docker-compose down

check: build
	docker-compose -p tests run mysite python3 manage.py makemigrations
	docker-compose -p tests run mysite python3 manage.py migrate
	docker-compose -p tests run mysite python3 manage.py test 