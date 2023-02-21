


#sorting


import pandas as pd
d=pd.read_excel(r"C:\Users\noori.zafar\Documents\python\data1.xlsx")
df=pd.DataFrame(d)
#print(df)


s=df.sort_values("Name")
print(s)



#sorting in descending order

import pandas as pd
d=pd.read_excel(r"C:\Users\noori.zafar\Documents\python\data1.xlsx")
df=pd.DataFrame(d)
#print(df)

s=df.sort_values('percent',ascending=False)

print(s)


#sorting in ascending order

import pandas as pd
d=pd.read_excel(r"C:\Users\noori.zafar\Documents\python\data1.xlsx")
df=pd.DataFrame(d)
#print(df)

s=df.sort_values('percent',ascending=True)

print(s)


#sorting based on 2 columns

import pandas as pd
d=pd.read_excel(r"C:\Users\noori.zafar\Documents\python\data1.xlsx")
df=pd.DataFrame(d)
#print(df)

s=df.sort_values(['percent','Name'],ascending=True)

print(s)


#0=ascending, 1= descending displaying different rows with different order

import pandas as pd
d=pd.read_excel(r"C:\Users\noori.zafar\Documents\python\data1.xlsx")
df=pd.DataFrame(d)
#print(df)

s=df.sort_values(['percent','Name'],ascending=[0,1])

print(s)










