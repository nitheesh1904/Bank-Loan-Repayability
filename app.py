from flask import Flask, render_template, request, redirect, url_for, flash
import pickle
import numpy as np
import keras
import json
import tensorflow as tf
import pandas as pd
from keras.models import model_from_json 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'awwfaw'

@app.route('/')
def index():
    print(5)
    return render_template("index.html")

@app.route("/home", methods=['GET','POST'])
def form():
    if request.method == 'POST':
        job_type = request.form['job_type'] 
        property = request.form['property'] 
        other_loans = request.form['other_loans'] 
        sab = request.form['sab'] 
        cab = request.form['cab'] 
        loan_history = request.form['loan_history'] 
        g_co = request.form['g_co'] 
        marital = request.form['marital'] 
        gender = request.form['gender'] 
        maintanence = request.form['maintanence'] 
        loan_amount = request.form['loan_amount'] 
        no_loans = request.form['no_loans'] 
        age = request.form['age'] 
        income = request.form['income'] 
        time = request.form['time']
        housing_type = request.form['housing_type']
        flash([job_type, property, other_loans, sab, cab, loan_amount, loan_history, no_loans, other_loans, g_co, marital, gender, maintanence, age, income, time, housing_type])

        if age<75:
            scaled_age=age/75
        else:
            scaled_age=1
        if no_loans<4:
            scaled_loan_count=no_loans/4
        else:
            scaled_loan_count=1
        
        if time<72:
            scaled_time=time/72
        else:
            scaled_time=1

        if income<4:
            scaled_income=income/4
        else:
            scaled_income=1
        if loan_amount<15672:
            scaled_loan_amount=loan_amount/15672
        else:
            scaled_loan_amount=1
        if maintanence<2:
            scaled_maintanence=maintanence/2
        else:
            scaled_maintanence=1       
        
        a=[scaled_maintanence,scaled_loan_amount,scaled_loan_count,scaled_age,scaled_income,scaled_time]

        if loan_history=='critical account':
            a.extend([1,0,0,0])
        elif loan_history=='delay in paying off loans in the past':
            a.extend([0,1,0,0])
        elif loan_history=='existing loans paid back duly till now':
            a.extend([0,0,1,0])
        elif loan_history=='no loans taken/all loans paid back duly':
            a.extend([0,0,0,1])

        if gender=='male':
            if marital=='single/divorced':
                a.extend([0,0,1])
            elif marital=='married':
                a.extend([0,1,0])

        elif gender=='female':
            a.extend([1,0,0])

        if cab=='between 0 and 200':
            a.extend([1,0,0])
        elif cab=='greater than 200':
            a.extend([0,1,0])
        elif cab=='less than 0/no account':
            a.extend([0,0,1])

        if sab=='above 500':
            a.extend([1,0,0])
        elif sab=='between 100 and 500':
            a.extend([0,1,0])
        elif sab=='less than 100':
            a.extend([0,0,1])

        if other_loans=='no':
            a.extend([1,0])
        elif other_loans=='yes':
            a.extend([0,1])

        if property=='no':
            a.extend([1,0])
        elif property=='yes':
            a.extend([0,1])

        if job_type=='self employed':
            a.extend([1,0,0,0])
        elif  job_type=='skilled':
            a.extend([0,1,0,0])
        elif job_type=='unemployed':
            a.extend([0,0,1,0])
        elif job_type=='unskilled':
            a.extend([0,0,0,1])

        if housing_type=='own':
            a.extend([1,0])
        elif housing_type=='rent':
            a.extend([0,1])

        if g_co=='co-applicant':
            a.extend([1,0,0])
        elif g_co=='gaurantor':
            a.extend([0,1,0])
        elif g_co=='none':
            a.extend([0,0,1])

        json_file = open('ml\model_final_tuned.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        a=a.flatten()
        array=np.array([a])
        check=pd.DataFrame(data=array)
        answer=np.round(loaded_model.predict(check))
        answer=answer.flatten()
        int(answer)

        

        return redirect(url_for('form'))
    return render_template("form.html")

if __name__ == "__main__":
    app.debug = True
    app.run()