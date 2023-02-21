

'''
#creating multiple index

import pandas as pd

l=[[1,2,3],['Noori','Ahad','Moin']]

mi=pd.MultiIndex.from_arrays(arrays,names=('ids','student'))

print(mi)'''


#converting dict to Dataframe

import pandas as pd

d={'name':['Noori','Ahad','Moin'],'age':[22,1,24]}
df=pd.DataFrame(d)

print(df)
