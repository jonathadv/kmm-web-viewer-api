# Send arguments to `docker build` command
DOCKER_ARGS ?=
DOCKER_IMAGE_NAME = kmymoney-web-viewer
DJANGO_PROJECT = kmmviewer
DJANGO_APP = kmm


# Default Option
default: help

# Install project packages from Pipfile
install:
	pipenv install

# Install project and development packages from Pipfile
install-dev:
	pipenv install --dev

# Start application
start:
	pipenv run uwsgi --ini uwsgi.ini

# Run dev server
dev-server:
	pipenv run python manage.py runserver 0.0.0.0:8000

# Run tests with `manage.py test`
test:
	set -e; pipenv run python manage.py test --verbosity=2;

# Run tests and coverage
test-cov:
	pipenv run coverage run manage.py test --verbosity=2;
	pipenv run coverage report

# Migrate Django and Kmm Models
migrate:
	pipenv run python manage.py migrate --database=kmm_db kmm; \
	pipenv run python manage.py migrate --database=django_db admin; \
	pipenv run python manage.py migrate --database=django_db auth; \
	pipenv run python manage.py migrate --database=django_db sessions; \
	pipenv run python manage.py migrate --database=django_db contenttypes; \


# Run pylint
lint:
	set -e; pipenv run pylint $(DJANGO_APP)/

# Sort imports as PEP8
isort:
	pipenv run isort $(DJANGO_APP)/**/*.py

# Format code with black
format:
	pipenv run black $(DJANGO_PROJECT) $(DJANGO_APP)/* --exclude 'migrations'

# Build image with using Dockerfile
docker-build:
	docker build $(DOCKER_ARGS) -t $(DOCKER_IMAGE_NAME) .

# Display this help
help:
	@ echo
	@ echo '  Usage:'
	@ echo ''
	@ echo '	make <target> [flags...]'
	@ echo ''
	@ echo '  Targets:'
	@ echo ''
	@ awk '/^#/{ comment = substr($$0,3) } comment && /^[a-zA-Z][a-zA-Z0-9_-]+ ?:/{ print "   ", $$1, comment }' ./Makefile | column -t -s ':' | sort
	@ echo ''
	@ echo '  Flags:'
	@ echo ''
	@ awk '/^#/{ comment = substr($$0,3) } comment && /^[a-zA-Z][a-zA-Z0-9_-]+ ?\?=/{ print "   ", $$1, $$2, comment }' ./Makefile | column -t -s '?=' | sort
	@ echo ''

