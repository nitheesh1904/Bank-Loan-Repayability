from flask import Flask, render_template, request, redirect, url_for, flash

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
        return redirect(url_for('form'))
    return render_template("form.html")

if __name__ == "__main__":
    app.debug = True
    app.run()