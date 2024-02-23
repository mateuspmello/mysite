build:
	docker-compose build

run: build
	docker-compose up

cleanup:
	docker-compose down

check: build
	docker-compose -p tests run mysite python manage.py test 

cov: build
	docker-compose -p tests run mysite python manage.py test --with-coverage
	
shell: build
	docker-compose -p tests run mysite python manage.py shell 