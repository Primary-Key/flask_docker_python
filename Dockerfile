FROM python:3.9.13-alpine
WORKDIR /app
ADD . /app
RUN pip3 install -r requirements_container.txt
CMD ["python3", "app.py"]