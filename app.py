from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import tensorflow as tf
import pandas as pd
from keras.models import model_from_json 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'awwfaw'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/bonus')
def bonus():
    return render_template("bonus.html")

global res
global bonus_scaled_loan_amount

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
        housing_type = request.form['housing_type']
        # all integer variables
        maintanence = int(request.form['maintanence'] )
        loan_amount = int(request.form['loan_amount'] )
        no_loans = int(request.form['no_loans'] )
        age = int(request.form['age'] )
        income = int(request.form['income'] )
        time = int(request.form['time'])

        if int(age)<75:
            scaled_age=age/75
        else:
            scaled_age=1
        if int(no_loans)<4:
            scaled_loan_count=no_loans/4
        else:
            scaled_loan_count=1
        
        if int(time)<72:
            scaled_time=time/72
        else:
            scaled_time=1

        if int(income)<4:
            scaled_income=income/4
        else:
            scaled_income=1
        if int(loan_amount)<15672:
            scaled_loan_amount=loan_amount/15672
        else:
            scaled_loan_amount=1
        if int(maintanence)<2:
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
        # flash(a)
        json_file = open('ml\model_final_tuned.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        array=np.array([a])
        # array=array.flatten()
        check=pd.DataFrame(data=array)
        answer=np.round(loaded_model.predict(check))
        answer=answer.flatten()
        global res
        res = int(answer)
        # flash(res)
        return redirect(url_for('result'))
    return render_template("form.html")

@app.route('/result')
def result():
    if res == 1:
        return render_template("success.html")
    else:
        return render_template("failure.html")

@app.route("/bonus-home", methods=['GET','POST'])
def bonus_form():
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
        housing_type = request.form['housing_type']
        # all integer variables
        maintanence = int(request.form['maintanence'] )
        no_loans = int(request.form['no_loans'] )
        age = int(request.form['age'] )
        income = int(request.form['income'] )
        time = int(request.form['time'])

        if int(age)<75:
            scaled_age=age/75
        else:
            scaled_age=1
        if int(no_loans)<4:
            scaled_loan_count=no_loans/4
        else:
            scaled_loan_count=1
        
        if int(time)<72:
            scaled_time=time/72
        else:
            scaled_time=1

        if int(income)<4:
            scaled_income=income/4
        else:
            scaled_income=1

        if int(maintanence)<2:
            scaled_maintanence=maintanence/2
        else:
            scaled_maintanence=1       
        
        a=[scaled_maintanence,0,scaled_loan_count,scaled_age,scaled_income,scaled_time]

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
        # flash(a)
        maxi=0
        global bonus_scaled_loan_amount
        bonus_scaled_loan_amount=0
        json_file = open('ml\model_final_tuned.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        for i in range(10,0,-1):
            a[1]=0.1*i
            array=np.array([a])
            check=pd.DataFrame(data=array)
            res = loaded_model.predict(check)
            if float(res[0][0])>maxi:
                maxi=res
                bonus_scaled_loan_amount=0.1*i
        return redirect(url_for('bonus_result'))
    return render_template("bonus-form.html")

@app.route('/bonus-result')
def bonus_result():
    global bonus_scaled_loan_amount
    result=bonus_scaled_loan_amount
    return render_template("bonus-result.html", resu=int(result*15000))

if __name__ == "__main__":
    app.debug = True
    app.run()