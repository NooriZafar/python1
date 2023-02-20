


#displaying the data using single condition

import pandas as pd
d=pd.read_csv(r"C:\Users\noori.zafar\Documents\python\data3.csv")
df=pd.DataFrame(d)
print(df)

s=df.loc[df['maths']<80]

print(s)


#using multiple condition to display data

import pandas as pd
d=pd.read_csv(r"C:\Users\noori.zafar\Documents\python\data3.csv")
df=pd.DataFrame(d)
print(df)

s=df.loc[(df['maths']<90) & (df['English']<90)]

print(s)

r=df.loc[(df['maths']<90) |(df['English']<90)]

print(r)


m=df.loc[(df['maths']<90) & (df['English']<90)& (df['c']<90)]

print(m)


#to display the string which contain the given substring,letters


import pandas as pd
d=pd.read_csv(r"C:\Users\noori.zafar\Documents\python\data3.csv")
df=pd.DataFrame(d)
print(df)

s=df.loc[df["Name"].str.contains('S')]

print(s)


#to display the string which doesn't contain the given substring,letters

import pandas as pd
d=pd.read_csv(r"C:\Users\noori.zafar\Documents\python\data3.csv")
df=pd.DataFrame(d)
print(df)

s=df.loc[~df["Name"].str.contains('S')]

print(s)


#to display the names starts with

import pandas as pd
d=pd.read_csv(r"C:\Users\noori.zafar\Documents\python\data3.csv")
df=pd.DataFrame(d)
print(df)

s=df.loc[df["Name"].str.startswith('S')]

print(s)


#display the names which doesn't starts with given letter or word

import pandas as pd
d=pd.read_csv(r"C:\Users\noori.zafar\Documents\python\data3.csv")
df=pd.DataFrame(d)
print(df)

s=df.loc[~df["Name"].str.startswith('M')]

print(s)



#to display the data thats end with given words/letters

import pandas as pd
d=pd.read_csv(r"C:\Users\noori.zafar\Documents\python\data3.csv")
df=pd.DataFrame(d)
print(df)

s=df.loc[df["Name"].str.endswith('i')]

print(s)


#calculating percentage

import pandas as pd
d=pd.read_csv(r"C:\Users\noori.zafar\Documents\python\data3.csv")
df=pd.DataFrame(d)
print(df)

df['total']=df['English']+df['maths']+df['c']

print(df)

df['percentage']=(df['total']/300)*100

print(df)


#providing gardes to the student based on marks


import pandas as pd
d=pd.read_csv(r"C:\Users\noori.zafar\Documents\python\data3.csv")
df=pd.DataFrame(d)
print(df)

df['total']=df['English']+df['maths']+df['c']

print(df)

df['percentage']=(df['total']/300)*100

print(df)

df['grade']='None'
print(df)

#display garde

df.loc[df['percentage']>90,['grade']]="DISTINCTION"

print(df)

#display grade to all students

df.loc[(df['percentage']>60) & (df['percentage']<90),['grade']]="FirstClass"

print(df)



#df.loc[df['percentage']>NaN,['grade']]="FAIL"

#print(df)







