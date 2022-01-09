#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 13:49:10 2022

@author: abhinav
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 16:16:54 2022

@author: abhinav
"""


import flasgger
import numpy as np
from flasgger import Swagger
import pickle
import json
from flask import Flask, request, jsonify
app = Flask(__name__)
Swagger(app)

model = pickle.load(open("model.pkl", 'rb'))


@app.route('/')
def welcome():
    return "BANK NOTE PREDICTION MODEL"


@app.route('/predict', methods=['GET'])
def predict():
    """Bank note authentication.
    ---
    parameters:
        - name: variance
          in: query
          type: number
          required: true
        - name: skewness
          in: query
          type: number
          required: true
        - name: curtosis
          in: query
          type: number
          required: true
        - name: entropy
          in: query
          type: number
          required: true
    responses:
        200:
            description: The output values
    """

    variance = request.args.get("variance")
    skewness = request.args.get("skewness")
    curtosis = request.args.get("curtosis")
    entropy = requst.args.get("entropy")

    prediction = model.predict([[variance, skewness, curtosis, entropy]])

    print(prediction)

    return "The  prediction is "+str(prediction)


if __name__ == "__main__":
    app.run(debug=True)
