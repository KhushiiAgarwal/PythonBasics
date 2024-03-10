import pandas as pd

r=['Roll no 1', 'Roll no 2', 'Roll no 3']

m=[70,95,80]

n=['Ram', 'Pam', 'Sam']

s={"Name":n, "Roll no":r, "Marks":m}

a=pd.DataFrame(s,columns=['Name', 'Marks'],

index=r)

print(a)

for a,b in a.iterrows():

print("*"*19)

print(b['Marks'])

print(b['Name'])
