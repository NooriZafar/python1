
'''
#accessinf/slicing

--head()--it display first 5 rows.

--head(3)-- display only 3 rows

--tail()--display last 5 rows

--tail(4)--display last 4 rows

--describe()--it display details of the table

--shape-- it display no. of rows and columns

--[start:stop:step]--slicing the table

--table['column_name']--to display single column

--table[[col1,col2]]--to diaplay multiple column

--tablename[[col1,col2]][start:stop:step]--to slice the column

--to get data in individual rows-- then we should use for loop

for inex,row in df.iterrows():
    print(index,row)

--to display single row--df.loc[1]

--to display the particular row

df.loc[df[colname]=='val']'''



import pandas as pd
d=pd.read_excel(r"C:\Users\noori.zafar\Documents\text1.xlsx")
df=pd.DataFrame(d)
print(df)

import pandas as pd
d=pd.read_excel(r"C:\Users\noori.zafar\Documents\text1.xlsx")
df=pd.DataFrame(d)

#to display only first 5 rows

df=df.head()
print(df)


import pandas as pd
d=pd.read_excel(r"C:\Users\noori.zafar\Documents\text1.xlsx")
df=pd.DataFrame(d)

#to display only first  rows

df=df.head(2)
print(df)



#to display last 5 rows

import pandas as pd
d=pd.read_excel(r"C:\Users\noori.zafar\Documents\text1.xlsx")
df=pd.DataFrame(d)

df=df.tail()
print(df)


#to display last 2 rows

import pandas as pd
d=pd.read_excel(r"C:\Users\noori.zafar\Documents\text1.xlsx")
df=pd.DataFrame(d)

df=df.tail(2)
print(df)



#to describe the table

import pandas as pd
d=pd.read_excel(r"C:\Users\noori.zafar\Documents\text1.xlsx")
df=pd.DataFrame(d)

df=df.describe()
print(df)


#to display number of columns

import pandas as pd
d=pd.read_excel(r"C:\Users\noori.zafar\Documents\text1.xlsx")
df=pd.DataFrame(d)

df=df.columns
print(df)


#to display shape

import pandas as pd
d=pd.read_excel(r"C:\Users\noori.zafar\Documents\text1.xlsx")
df=pd.DataFrame(d)

df=df.shape
print(df)


#displaying single row

import pandas as pd
d=pd.read_excel(r"C:\Users\noori.zafar\Documents\text1.xlsx")
df=pd.DataFrame(d)

df=df['Name']

#df1=df['Name','age'].head() #display only 5 rows

print(df)
#print(df1)



#display rows using slicing method

import pandas as pd
d=pd.read_excel(r"C:\Users\noori.zafar\Documents\text1.xlsx")
df=pd.DataFrame(d)

df=df[1:4:2]
print(df)

df1=df['Name'][1:3]

print(df1)


#display single row

import pandas as pd
d=pd.read_excel(r"C:\Users\noori.zafar\Documents\text1.xlsx")
df=pd.DataFrame(d)

singlerow=df.loc[1]
#singlerow=df.loc[1:3]

print(singlerow)


#to get all the rows details one by one


import pandas as pd
d=pd.read_excel(r"C:\Users\noori.zafar\Documents\text1.xlsx")
df=pd.DataFrame(d)

for i,row in df.iterrows():
    print(i,row)



#to check/display particular data


import pandas as pd
d=pd.read_excel(r"C:\Users\noori.zafar\Documents\text1.xlsx")
df=pd.DataFrame(d)

s=df.loc[df['Name']=='pavi']

print(s)


import pandas as pd
d=pd.read_excel(r"C:\Users\noori.zafar\Documents\text1.xlsx")
df=pd.DataFrame(d)

s=df.loc[df['Name']=='Pavi']

print(s)








