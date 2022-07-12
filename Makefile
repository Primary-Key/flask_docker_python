install:
	pip3 install --upgrade pip &&\
		pip install -r requirements.txt         

lint:
	pylint --disable=R,C,W1203,W0702 app.py

build:
	docker build -t flask-docker-python .

run:
	docker rm -f python-container
	docker run -d --name python-container -p 3200:3200 flask-docker-python

test:
	python3 -m pytest -vv --cov=app test_app.py

all: install lint build run test

test_all: lint build run test