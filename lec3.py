'''This lecture is regarding advance method in python'''
import pandas as pd

# Creating a DataFrame based on the provided data
data = {
    "Name": ["Raman", "Raman", "Raman",
                      "Zuhaire", "Zuhaire", "Zuhaire",
                      "Aashravy", "Aashravy", "Aashravy",
                      "Mishti", "Mishti", "Mishti"],
    "UT": [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
    "Maths": [22, 21, 14, 20, 23, 22, 23, 24, 12, 15, 18, 17],
    "Science": [21, 20, 19, 17, 22, 21, 19, 20, 15, 22, 25, 18],
    "S.St.": [18, 17, 15, 22, 25, 20, 20, 22, 20, 20, 20, 20],
    "Hindi": [20, 22, 24, 21, 25, 24, 15, 17, 22, 22, 24, 25],
    "Eng": [21, 24, 23, 23, 25, 25, 22, 20, 22, 23, 21, 20],
}

df = pd.DataFrame(data)
print(df)


'''.max() is use to find maximum value of column data regardless of 
data type'''

df_max_of_data=df.max()
print(df_max_of_data)

#for numeric data we use .max(numeric_only=True)
print(df.max(numeric_only=True))

"""To get the data who got most in unit 2"""
Name=df[df['Maths']==df["Maths"].max()]['Name']
print(Name)

"""To get maximum in row wise .max(axis=1)"""
print(df.max(axis=1,numeric_only=True))  


"""All thing is same for minimum .min()"""


""".sum() is use to add all element of columns data regardless of 
datatype

sum(numeric_only=Fales,axis=0)"""

df_sum=df.sum(numeric_only=True)
print(df_sum)

""".count() count number of data in column unless axis is specify"""
df_Count=df.count()
print(df_Count)

""".mean()
   .mode()
   .median()
   .quantile(q= fraction of part of one) if q=0.25 it give 25th percentile 
   data,rest do as name suggest
   .var() for variance 
   .std() standard deviation"""


""".aggregate() helps us to get max,min,count,std,var at once"""


df_af=df["Maths"].aggregate(['max','min','count'])
print(df_af)