#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/message', methods=['POST'])
def message():
    name = request.json['name']
    return jsonify({'message': f'Hello {name}'})


@app.route('/health', methods=['GET'])
def health():
    return 'OK'


# Return errors as JSON objects
def app_error(e):
    return jsonify({'message': str(e)}), 400


if __name__ == '__main__':
    app.register_error_handler(Exception, app_error)
    app.run(host='0.0.0.0', port=8080)
