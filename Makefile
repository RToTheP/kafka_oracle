SHELL := bash

start_colima:
	./scripts/start_colima.sh

stop_colima:
	./scripts/stop_colima.sh

db_up:
	docker-compose -f docker/docker-compose.oracle.yaml up -d

db_down:
	docker-compose -f docker/docker-compose.oracle.yaml down --remove-orphans

up:
	docker-compose -f docker/docker-compose.kafka.yaml -f docker/docker-compose.oracle.yaml -f docker/docker-compose.ui.yaml -f docker/docker-compose.connect.yaml up -d

down:
	docker-compose -f docker/docker-compose.kafka.yaml -f docker/docker-compose.oracle.yaml -f docker/docker-compose.ui.yaml -f docker/docker-compose.connect.yaml down --remove-orphans

build:
	docker-compose -f docker/docker-compose.test.yaml build

logs:
	docker-compose -f docker/docker-compose.kafka.yaml -f docker/docker-compose.oracle.yaml -f docker/docker-compose.ui.yaml logs

docker_integration_test:
	docker-compose -f docker/docker-compose.kafka.yaml -f docker/docker-compose.oracle.yaml -f docker/docker-compose.test.yaml up --exit-code-from code code

docker_integration_test_logs:
	docker-compose -f docker/docker-compose.kafka.yaml -f docker/docker-compose.oracle.yaml -f docker/docker-compose.test.yaml logs code