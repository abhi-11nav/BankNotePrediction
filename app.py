#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 21:19:14 2021

@author: abhinav
"""

from flask import Flask,request,render_template
import numpy as np 
import pandas as pd
import pickle
import sklearn

app = Flask(__name__,template_folder='template')

model = pickle.load(open('decision_tree_classifier.pkl','rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        variance = float(request.form['variance'])
        skewness = float(request.form['skewness'])
        curtosis = float(request.form['curtosis'])
        entropy  = float(request.form['entropy'])
        
        prediction = model.predict([[variance,skewness,curtosis,entropy]])
        
        output = round(prediction[0],2)
        
        if output<0:
            return render_template('/index.html',prediction_text = "Your note is not valid")
        else:
            return render_template('/index.html',prediction_text = "Your note is valid congratulations")
        
     
if __name__ == "__main__":
    app.run(debug=True)
    
    