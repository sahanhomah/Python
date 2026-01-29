import pandas as pd
a=pd.Series([1,2,3,4,5], index=['a', 'b', 'c', 'd', 'e'])
print(a)

b=pd.DataFrame({'Name':['Alice','Sahan','Shrestha'],
                'Age':[24,22,23],})
b['Grade'] = ['A', 'A+', 'A']
print(b)    
print(b['Name'])
print(b.head())
df=pd.read_csv('data_info.csv')
print(df['age'])
new_data = pd.DataFrame({
    'student_id': [6969],
    'name': ['rameshyadav'],
    'age': [92],
    'gender':['male'],
    'course':['doctor'],
    'semester':['final'],
    'marks':[100],
    'email':['sahanshrestha2000@gmail.com']
})
new_data.to_csv("data_info.csv", mode='a', header=False, index=False, lineterminator='\n')
