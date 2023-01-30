# Skew- Loan Repayment Calculator

Skew is a dynamic web-app made using Python Flask that enables a user to check if they would be able to repay the loan they have borrowed or not. With the help of AI/ML and Deep Learning, the website also predicts the ideal loan amount one should borrow based on a few details that the user provides.


# Features

- Skew predicts the scope of repayment of a borrower with a Deep Learning ML model with over 90% accuracy. 
- It can suggest a loan amount range that the borrower can borrow from such that the borrower has the highest scope of repayment

## Requirements
 - `Python3`: Python 3.8 (64bit) or newer
	 - Flask: 2.2.2 or newer
	 - Psycopg2-binary: 2.9.5 or newer
	 - Gunicorn: 20.1.0 or newer
	 - Numpy: 2.24.1 or newer
	 - Pandas: 1.5.3 or newer
	 - Scikit-learn: 1.2.1 or newer
	 - Tensorflow: 2.11.0 or newer

## Usage
Clone the repository into your local computer using Git CLI or the link provided above.
In your terminal, run the following command:

    pipenv shell
    pip install -r requirements.txt
 
 If the above command doesn't work, you can install all modules required individually by running:
 

    pipenv install Flask

Once all modules are installed, the local server can be started by running:

    python app.py


## Screenshots
### Homepage
![Home page](/static/images/ss/home.png)
### Form
![Home page](/static/images/ss/form.png)
### Result Page
![Home page](/static/images/ss/result.png)
### Loan Amount Calculator
![Home page](/static/images/ss/bonus.png)
### Loan Amount Calculator- Result
![Home page](/static/images/ss/bonus-result.png)

## Known Issues
The website has not been succesfully deployed yet. The website has been hosted for free with the help of Render, and can be viewed [here](loan-repayment-calculator.onrender.com/). The website currently shows an internal server error upon entering all the details of the user and submitting the user input.