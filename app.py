from flask import Flask, render_template, make_response, jsonify, request
import sqlite3 as sl

app = Flask(__name__)


PORT = 3200
HOST = '0.0.0.0'

DATA = {}

# GET METHOD

@app.route("/")
def home():
  return "<h1 style='color:blue'>This is home.</h1>"

@app.route("/temp")
def template():
  return render_template('index.html')

@app.route("/qstr")
def query_string():
  if request.args:
    req = request.args
    res = {}
    for key, val in req.items():
      res[key] = val
    res = make_response(jsonify(res), 200)
    return res

  res = make_response({"error":"No query string"}, 400)
  return res

@app.route("/json")
def get_json():
    res = make_response(jsonify(DATA), 200)
    return res

@app.route("/json/<collection>/<member>")
def get_data(collection, member):
  if collection in DATA:
    member = DATA[collection].get(member)
    if member:
      res = make_response(jsonify({"res":member}), 200)
      return res
    
    res = make_response(jsonify({"error":"Member not found"}), 400)
    return res

  res = make_response(jsonify({"error":"Collection not found"}), 400)
  return res

# POST METHOD

@app.route("/json/<collection>", methods=["POST"])
def create_collection(collection):
  req = request.get_json()

  if collection in DATA:
    res = make_response(jsonify({"error":"collection already exists"}), 400)
    return res

  DATA.update({collection: req})
  res = make_response(jsonify({"res":"collection created"}), 201)
  return res

# PUT METHOD

@app.route("/json/<collection>/<member>", methods=["PUT"])
def update_collection(collection, member):
  req = request.get_json()

  if collection in DATA:
    if member:
      DATA[collection][member] = req["new"]
      res = make_response(jsonify({"res":DATA[collection]}), 200)
      return res

    res = make_response(jsonify({"error":"Member not specified"}), 400)
    return res
  
  res = make_response(jsonify({"error":"Collection not found"}), 400)
  return res

@app.route("/json/<collection>", methods=["DELETE"])
def delete_collection(collection):
  if collection in DATA:
    del DATA[collection]
    res = make_response(jsonify(DATA), 200)
    return res
      
  res = make_response(jsonify({"error":"Collection not found"}), 400)
  return res

@app.route("/reset", methods=["DELETE"])
def reset():
  DATA.clear()
  res = make_response(jsonify({"res":"Deleted all data"}), 200)
  return res

if __name__ == "__main__":
  app.run(host=HOST, port=PORT)
