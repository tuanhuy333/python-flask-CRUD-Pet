#!/usr/bin/env python3

import connexion
from flask import Flask, render_template
from flask_cors import CORS, cross_origin

from swagger_server import encoder

# app = Flask(__name__)
app = connexion.App(__name__, specification_dir='./swagger/')

@app.route('/test')
@cross_origin()  # Route specific CORS via decorator
def method_name():
    return render_template("create.html")


def main():
   
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Pet Store'}, pythonic_params=True)
    # Allow requests from everywhere
    CORS(app.app)
    app.run(port=8080)


if __name__ == '__main__':
    main()
