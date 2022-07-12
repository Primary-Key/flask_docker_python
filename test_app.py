from flask import jsonify
import requests

# LOCAL TESTS



# DOCKER TESTS

def test_docker_json_request():
  requests.delete("http://localhost:3200/reset")
  response = requests.get("http://localhost:3200/json")
  assert response.json() == {}

def test_docker_create_collection():
  requests.delete("http://localhost:3200/reset")
  address = 'http://localhost:3200/json/cars'
  input_json = {
    "f":"ferrari",
    "p":"porche",
    "m":"mazda"
  }
  ok_resp = {
    "res": "collection created"
  }
  response = requests.post(address, json = input_json)
  assert response.json() == ok_resp

def test_docker_duplicate_collection():
  requests.delete("http://localhost:3200/reset")
  address = 'http://localhost:3200/json/cars'
  input_json = {
    "f":"ferrari",
    "p":"porche",
    "m":"mazda"
  }
  exp_ok_resp = {"res": "collection created"}
  exp_err_resp = {"error":"collection already exists"}
  ok_resp = requests.post(address, json = input_json)
  assert ok_resp.status_code == 201
  assert ok_resp.json() == exp_ok_resp

  error_resp = requests.post(address, json = input_json)
  assert error_resp.status_code == 400
  assert error_resp.json() == exp_err_resp

def test_docker_create_coll_get_coll():
  requests.delete("http://localhost:3200/reset")
  address = 'http://localhost:3200/json/banana'
  input_json = {
    "b": 42,
  }
  ok_resp = {
    "res": "collection created"
  }
  response = requests.post(address, json = input_json)
  assert response.json() == ok_resp

  ok_resp = {
    "res": 42
  }
  address = 'http://localhost:3200/json/banana/b'
  response = requests.get(address)
  assert response.json() == ok_resp