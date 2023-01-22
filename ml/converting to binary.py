
a=[]

if Loan History=='critical account':
    a.extend(1,0,0,0)
elif Loan History=='delay in paying off loans in the past':
    a.extend(0,1,0,0)
elif Loan History=='existing loans paid back duly till now':
    a.extend(0,0,1,0)
elif Loan History=='no loans taken/all loans paid back duly':
    a.extend(0,0,0,1)

if amount in current account=='between 0 and 200':
    a.extend(1,0,0)
 elif amount in current account=='greater than 200':
    a.extend(0,1,0)
elif amount in current account=='less than 0/no account':
    a.extend(0,0,1)

if amount in savings account=='above 500':
    a.extend(1,0,0)
elif amount in savings account=='between 100 and 500':
    a.extend(0,1,0)
elif amount in savings account=='less than 100':
    a.extend(0,0,1)

if Other loans plans taken=='no':
    a.extend(1,0)
elif Other loans plans taken=='yes':
    a.extend(0,1)

if Owned property=='no':
    a.extend(1,0)
elif Owned property=='yes':
    a.extend(0,1)

if Type of job performed=='self employed':
    a.extend(1,0,0,0)
elif  Type of job performed=='skilled':
    a.extend(0,1,0,0)
elif Type of job performed=='unemployed':
    a.extend(0,0,1,0)
elif Type of job performed=='unskilled':
    a.extend(0,0,0,1)

if Type of Housing=='own':
    a.extend(1,0)
elif Type of Housing_own=='rent':
    a.extend(0,1)

if Guarantor or Debtor=='co-applicant':
    a.extend(1,0,0)
elif Guarantor or Debtor=='gaurantor':
    a.extend(0,1,0)
elif Guarantor or Debtor=='none':
    a.extend(0,0,1)

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
final=scaler.fit_transform(a)