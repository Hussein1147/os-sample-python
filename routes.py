import unicodedata
import sys, os,json
from flask import Flask, jsonify, Response, request
from flask_security import auth_token_required, http_auth_required
from Models import app, user_datastore,User,db,Transfers
from sqlalchemy.exc import IntegrityError,InvalidRequestError



@app.route("/")
def hello():
    return "Hello World dear"

@app.route('/dummy-api')
def dummyAPI():
    dict = {
        "Key1": "Value1",
        "Key2": "value2"
    }
    return jsonify(items=dict)