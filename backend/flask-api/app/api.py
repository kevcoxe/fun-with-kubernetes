import os

from flask import jsonify
from app import app


products = [
    {
        'name': 'macbook pro',
        'description': 'This is my old work computer I am looking to sell',
        'price': 810
    },
]


@app.route('/')
def index():
    return 'success'


@app.route("/api")
def api_v1_get_version():
    version = os.getenv('API_VERSION')
    return jsonify({
        'message': 'Version',
        'data': version,
    }), 200


@app.route("/api/products")
def api_v1_get_products():
    return jsonify({
        'message': 'Here are my products',
        'data': products,
    }), 200
