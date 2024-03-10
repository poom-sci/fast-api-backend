build-docker:
	docker build -t todo-api:v1 .

run-docker-compose:
	docker-compose up

run-dev:
	uvicorn main:app --reload

save-pip-requirements:
	pip freeze > requirements.txt

lint-check:
	ruff check .

lint:
	ruff format .