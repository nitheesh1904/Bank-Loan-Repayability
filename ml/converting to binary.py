
a=[]

if loan_history=='critical account':
    a.extend(1,0,0,0)
elif loan_history=='delay in paying off loans in the past':
    a.extend(0,1,0,0)
elif loan_history=='existing loans paid back duly till now':
    a.extend(0,0,1,0)
elif loan_history=='no loans taken/all loans paid back duly':
    a.extend(0,0,0,1)

if cab=='between 0 and 200':
    a.extend(1,0,0)
 elif cab=='greater than 200':
    a.extend(0,1,0)
elif cab=='less than 0/no account':
    a.extend(0,0,1)

if sab=='above 500':
    a.extend(1,0,0)
elif sab=='between 100 and 500':
    a.extend(0,1,0)
elif sab=='less than 100':
    a.extend(0,0,1)

if other_loans=='no':
    a.extend(1,0)
elif other_loans=='yes':
    a.extend(0,1)

if property=='no':
    a.extend(1,0)
elif property=='yes':
    a.extend(0,1)

if job_type=='self employed':
    a.extend([1,0,0,0])
elif  job_type=='skilled':
    a.extend(0,1,0,0)
elif job_type=='unemployed':
    a.extend(0,0,1,0)
elif job_type=='unskilled':
    a.extend(0,0,0,1)

if housing_type=='own':
    a.extend(1,0)
elif housing_type=='rent':
    a.extend(0,1)

if g_co=='co-applicant':
    a.extend(1,0,0)
elif g_co=='gaurantor':
    a.extend(0,1,0)
elif g_co=='none':
    a.extend(0,0,1)
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
final=scaler.fit_transform(a)
