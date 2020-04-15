
from flask import jsonify
from app import app


products = [
    {
        'nam': 'macbook pro',
        'description': 'This is my old work computer I am looking to sell',
        'price': 810
    },
]


@app.route("/products")
def api_v1_get_products():
    return jsonify({
        'message': 'Here are my products',
        'data': products,
    }), 200
