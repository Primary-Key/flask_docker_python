# flask_docker_python

## setup

`pip3 install virtualenv`

`virtualenv -p python3 docker_flask`

`source docker_flask/bin/activate`

`pip3 install flask`

`pip3 freeze > requirements.txt`

## developing and testing

`python3 app.py`       

`brew install npm`

`npm install -g nodemon`

`nodemon app.py`

## docker

`docker build -t flask-docker-python .`

`docker run -d --name python-container -p 3200:3200 flask-docker-python`

`docker ps -a`
