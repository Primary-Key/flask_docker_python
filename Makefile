install:
	pip3 install --upgrade pip &&\
		pip install -r requirements_container.txt         

lint:
	pylint --disable=R,C,W1203,W0702 app.py

build:
	docker build -t flask-docker-python .

run: stop
	docker run -d --name python-container -p 3200:3200 flask-docker-python

stop:
	docker rm -f python-container

test:
	python3 -m pytest -vv test_app.py

all: install lint build run test

test_all: lint build run test