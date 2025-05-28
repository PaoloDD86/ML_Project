'''Applicativo web in Flask che serve per raccogliere dati da un form HTML,
passarli a una pipeline di predizione (modello ML), ed esporre il risultato all’utente
Cosa mi serve?
Flask: framework per creare app web leggere in Python.
request: per leggere i dati ricevuti dal form web.
render_template: per mostrare pagine HTML.
CustomData e PredictPipeline: sono le classi del tuo codice ML che:
1-raccolgono dati utente (CustomData)
2-fanno predizioni (PredictPipeline)
'''

from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application
#Route for a home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))
        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        
        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(pred_df)
        
        return render_template('home.html',results=results[0])

# Avvio dell'APP
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)
