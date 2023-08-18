SHELL := bash

start_colima:
	./start_colima.sh

stop_colima:
	./stop_colima.sh

up:
	docker-compose -f docker/docker-compose.yaml up

down:
	docker-compose -f docker/docker-compose.yaml down --remove-orphans

build:
	docker-compose -f docker/docker-compose.yaml build

logs:
	docker-compose -f docker/docker-compose.yaml logs

run_integration_tests:
	docker-compose -f docker/docker-compose.yaml up --exit-code-from code code