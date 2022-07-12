import requests

OK_JSON = {
    'languages':{
        'es':'Spanish',
        'en':'English',
        'fr':'French',
    },
    'colors':{
        'r':'red',
        'g':'green',
        'b':'blue',
    },
    'couds':{
        'IBM':'IBM Cloud',
        'AMAZON': 'AWS',
        'MICROSOFT': 'AZURE'
    }
}

# LOCAL TESTS

# DOCKER TESTS

def test_docker_json_request():
  response = requests.get("http://localhost:3200/json")
  assert response.json() == OK_JSON

def test_docker_create_collection():
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