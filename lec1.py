'''Today we are going to make pandas DataFrame using different 
Data list of pandas'''

#Using 2D list each element inside list act as data of row

import pandas as pd 

list_of_data=[[1,2,3],[4,5,6],[7,8,9]]
DataFrame_of_data=pd.DataFrame(list_of_data,dtype="int32")
print(DataFrame_of_data)

#Using dictionary of list key is use as column name as list as column

import pandas as pd

dic_of_data={10:['abhay','manish','ravis'],11:[90,99,85]}
DataFrame_of_data=pd.DataFrame(dic_of_data)
print(DataFrame_of_data)

#Using array or series is same as list replace in above theory 

import pandas as pd
import numpy as np

Data1=pd.Series([1,2,3,4,5])
Data2=np.array([4,5,6,7,8])

dic_of_data={1:Data1,2:Data2}
print(pd.DataFrame(dic_of_data))

"""Required argument in DataFrame is (object,columns,index,dtype)"""

#Making DataFrame using Dictionary of Dictionary 

import pandas as pd
import numpy as np

dic_of_data={1:{'name':'abhay','roll_no':1,'marks':34},
             2:{'name':'HARSH','roll_no':2,'marks':44},
             3:{'name':'mansih','roll_no':3,'marks':54}}

"""By default is we use DataFrame it make first level key as column name 
and 2nd level row index and we have to repeat 2nd level key as it store only one data"""

DataFrame_of_data=pd.DataFrame(dic_of_data)
print(DataFrame_of_data)


#Making DataFrame using CSVfile in pandas

import pandas as pd

df=pd.read_csv(r'data.csv',sep=',',header=None)
print(df)

"""pd.read_csv(<file_path>,header=<int/None>,sep="<char>,dtype={col1:"int32",col2:"float64"}
,index=[lsit of index name])"""


#Making DataFrame using excel sheet 

import pandas as pd

df=pd.read_excel(r'Book1.xlsx')
print(df)
