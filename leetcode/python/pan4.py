

#to add the new column

import pandas as pd
d=pd.read_excel(r"C:\Users\noori.zafar\Documents\python\data2.xlsx")
df=pd.DataFrame(d)

print(df)

df['Total_marks']=0
print(df)


df['Total_marks']=df['English']+df['maths']+df['c']

#print(s)


#to remove the column

import pandas as pd
d=pd.read_excel(r"C:\Users\noori.zafar\Documents\python\data2.xlsx")
df=pd.DataFrame(d)

print(df)

s=df.drop(columns='maths')

print(s)


#to know the highest marks

import pandas as pd
d=pd.read_excel(r"C:\Users\noori.zafar\Documents\python\data2.xlsx")
df=pd.DataFrame(d)

df['Total_marks']=df['English']+df['maths']+df['c']
print(df)

#s=df.[['Name','Total_marks']]--display only marks and name

s=df.sort_values(['Name','Total_marks'],ascending=True)


print(s.head(1))



#removing the rows with missing data--and the original data is not reflected

import pandas as pd
d=pd.read_excel(r"C:\Users\noori.zafar\Documents\python\missingdata.xlsx")
df=pd.DataFrame(d)
print(df)

s=df.dropna()
print(s)


#if we want to reflect the original data and remove null rows


import pandas as pd
d=pd.read_excel(r"C:\Users\noori.zafar\Documents\python\missingdata.xlsx")
df=pd.DataFrame(d)
print(df)

s=df.dropna(inplace=True)
print(s)

print(df)#here data is removed


#to remove single row null value

import pandas as pd
d=pd.read_excel(r"C:\Users\noori.zafar\Documents\python\missingdata.xlsx")
df=pd.DataFrame(d)
print(df)

s=df['maths'].dropna()
print(s)


s=df.loc[:,['English','maths']].dropna()
print(s)


#filling missing values

import pandas as pd
d=pd.read_excel(r"C:\Users\noori.zafar\Documents\python\missingdata.xlsx")
df=pd.DataFrame(d)
print(df)

s=df.fillna('MISSING')#replace the empty boxex with word missing

print(s)


#replacing the missing value

import pandas as pd
d=pd.read_excel(r"C:\Users\noori.zafar\Documents\python\missingdata.xlsx")
df=pd.DataFrame(d)
print(df)

s=df.fillna(40)
print(s)


#filling missing value by average value

import pandas as pd
d=pd.read_excel(r"C:\Users\noori.zafar\Documents\python\missingdata.xlsx")
df=pd.DataFrame(d)
print(df)


s=df['maths'].fillna(df['maths'].mean())
print(s)


#using floor function

import math

import pandas as pd
d=pd.read_excel(r"C:\Users\noori.zafar\Documents\python\missingdata.xlsx")
df=pd.DataFrame(d)
print(df)


s=df['maths'].fillna(math.floor(df['maths'].mean()))
print(s)


#checking for duplicate values


import pandas as pd
d=pd.read_excel(r"C:\Users\noori.zafar\Documents\python\missingdata.xlsx")
df=pd.DataFrame(d)
print(df)

s=df.duplicated()#check we have duplicate values or not.if exit it return as true or else false

print(s)


#removing duplicate values

import pandas as pd
d=pd.read_excel(r"C:\Users\noori.zafar\Documents\python\data2.xlsx")
df=pd.DataFrame(d)
print(df)


s=df.drop_duplicates()
print(s)
