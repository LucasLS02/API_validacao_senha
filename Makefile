.PHONY: params install-and-run run

install-and-run:
	docker-compose -f docker-compose.yaml up --build --force-recreate

run:
	docker-compose -f docker-compose.yaml up