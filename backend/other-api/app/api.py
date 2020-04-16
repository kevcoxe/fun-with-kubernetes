import os
import requests

from flask import jsonify
from app import app


FLASK_API_SERVICE_HOST = os.getenv('FLASK_API_SERVICE_HOST', 'http://localhost')
FLASK_API_SERVICE_PORT = os.getenv('FLASK_API_SERVICE_PORT', '5000')


def get_products():
    url = 'http://{host}:{port}{route}'.format(
        host=FLASK_API_SERVICE_HOST,
        port=FLASK_API_SERVICE_PORT,
        route='/api/products'
    )
    r = requests.get(url)
    json_response = r.json()
    return json_response


@app.route('/')
def index():
    return 'success', 200


@app.route('/env')
def api_get_env():
    try:
        return jsonify({
            'message': 'here are the environment variables',
            'data': dict(os.environ)
        }), 200

    except Exception as e:
        print('error: {}'.format(e))
        return jsonify({
            'message': 'could not get environment variables',
            'error': 'error: {}'.format(e)
        }), 500


@app.route('/products')
def api_get_products():
    try:
        return jsonify(get_products()), 200
    except Exception as e:
        print('error: {}'.format(e))
        return jsonify({
            'message': 'could not get products',
            'error': 'error: {}'.format(e)
        }), 500
