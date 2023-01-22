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
        gender = request.form['gender'] 
        flash(gender, 'success')
        return redirect(url_for('index'))
    return render_template("form.html")

if __name__ == "__main__":
    app.debug = True
    app.run()