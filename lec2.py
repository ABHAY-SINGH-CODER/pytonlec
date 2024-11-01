'''Today we are going to learn some operation on rows of the DataFrame'''

import pandas as pd

list_of_data=[{'name':"Abhay Singh","Roll No":20200127428},
              {'name':"Vivek Singh","Roll No":20200127427},
              {'name':"Ramesh Singh","Roll No":20200137428}]

df=pd.DataFrame( list_of_data)

for index,row in df.iterrows():
    #.iterrows return (index,row in Series type)
    print(index,row["name"],row['Roll No'])
    

print("\n")

"""Now accessing row element using name tuple it is faster than above method"""
for row in df.itertuples():
    #Even though you have saved roll no as "Roll No" but when this 
    #function encounter white space in name of column it change it as _(position) here is 2
    print(getattr(row,'_2'))

'''Here will try to get row data using condition '''
import pandas as pd

  

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jack'],
    'Age': [24, 22, 23, 21, 20, 23, 22, 24, 21, 22],
    'Score': [85, 92, 78, 89, 95, 70, 88, 76, 90, 84],
    'Subject': ['Math', 'Physics', 'Chemistry', 'Math', 'Biology', 'Chemistry', 'Math', 'Physics', 'Biology', 'Chemistry'],
    'Passed': [True, True, False, True, True, False, True, False, True, True]
}

df = pd.DataFrame(data)

print(df)

passed_students=df[df['Score']>70]
print(passed_students)

