SHELL := bash

start_colima:
	./start_colima.sh

stop_colima:
	./stop_colima.sh

up:
	docker-compose -f docker/docker-compose.yaml -f docker/docker-compose.ui.yaml up -d

down:
	docker-compose -f docker/docker-compose.yaml -f docker/docker-compose.ui.yaml down --remove-orphans

build:
	docker-compose -f docker/docker-compose.test.yaml build

logs:
	docker-compose -f docker/docker-compose.yaml -f docker/docker-compose.ui.yaml logs

docker_integration_test:
	docker-compose -f docker/docker-compose.yaml -f docker/docker-compose.test.yaml up --exit-code-from code code

docker_integration_test_logs:
	docker-compose -f docker/docker-compose.yaml -f docker/docker-compose.test.yaml logs code