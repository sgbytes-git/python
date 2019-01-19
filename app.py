# -*- coding: utf-8 -*-

from flask import Flask, make_response, request


app = Flask(__name__)

# TODO add your actions below
@app.route('/')
def generate():
    return 'Hello world'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
