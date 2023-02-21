'''

Pandas:

Pandas is a Python library used for working with data sets.

It has functions for analyzing, cleaning, exploring, and manipulating data.

more flexible
--represent data in rows and columns,works on missing value,indexing,slicing,subsetting the large data sets
--merge and join 2 different data set esly.

What pandas do


--Is there a correlation between two or more columns?
--What is average value?
--Max value?
--Min value?
--Pandas are also able to delete rows that are not relevant,
or contains wrong values, like empty or NULL values. This is called cleaning the data.


Pandas uses 3 data stucture


1.series--in this data is represented in one dimensional array-- list or any one dimensional array  as example

2.dataframe-- 2 dimensional-- example as list,dict,series or another dataframe

3.panel--multi dimensional-- example are majar axis,n\minor axis


'''


'''
SERIES:::::

syntax:  pd.Series(data,index)

import pandas as pd

l=[1,2,3,4,5]

s=pd.Series(l)
print(s) #it takes default index values if me not mention

#to give user inex vales

s=pd.Series(l,index=['a','b','c','d','e'])

print(s)


Creating series in different ways:

--empty series:

import pandas as pd

s=pd.Series()
print(s)

--series using array: before creating array import numpy

import pandas as pd
import numpy as np
a=np.array([1,2,3,4])#array is space seperated value
print(a)

s=pd.Series(a)
print(s)



--series using list:


l=[10,20,30]
s=pd.Series(l)
print(s)

--series using dictionary:


import pandas as pd

d={'a':'10','b':'20','c':'30'}

s=pd.Series(d)
print(s)


--dict can also b represented as list of tuples.we can create series using list of tuples:

dt=[('a',10),('b',20)]
s=pd.Series(dt)

print(s)

'''



'''DATAFRAME:::::

syntax:pd.DataFrame(data)


import pandas as pd

d={'Name':['Noori','Moin','Neelu'],'Percentage':[90,99,90]}

print(pd.DataFrame(d))

--Different ways of creating dataframe:

1. load data from excel file:

syntax:pd.read_excel("path")


import pandas as pd

d=pd.read_excel("C:\\Users\\noori.zafar\\Downloads\\data.csv")#we are using \\ to get the output
print(d)
s=pd.DataFrame(d)
print(s)


2. load data from csv file:

syntax:pd.read_csv("path")

import pandas as pd

df = pd.read_csv(r"C:\Users\noori.zafar\Documents\text1.csv")

print(df.to_string())


3. create data frame using dictionary:


d={'Name':['Noori','Moin','Neelu'],'Percentage':[90,99,90]}
print(d)

df=pd.DataFrame(d)

print(df)

4. create data frame from list of tuples

'''

'''

#import pandas

import pandas as pd

print(pd.__version__)

data = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}


print(data)# display as set data

pandadata = pd.DataFrame(data)



print("------------")
print(pandadata) # display as table




import pandas as pd

df = pd.read_csv(r"data.csv")

print(df.to_string())





import pandas as pd

d=pd.read_csv(r"C:\Users\noori.zafar\Documents\text1.csv")
df=pd.DataFrame(d)
print(df)'''




