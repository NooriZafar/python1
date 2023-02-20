

'''d={'Name':['Noori','Moin','Neelu'],'Percentage':[90,99,90]}
print(d)

df=pd.DataFrame(d)

print(df)'''


'''Attributes in series:


--index: Series.index-return all index values

--array: Series.array--return array of values

--values: Series.values-- return values of series

--name: Series.name-- return name of series

--shape: Series.shape-- return shape 

--ndim: Series.ndim-- return the dimension of series

--size: Series.size-- return the size of series

--nbytes: Series.nbytes-- returns the memory accupied by values

--memory_usay(): Series.memory_usage()-- returns memory accupied by both index
                                         and values.


--empty: Series.empty-- returns true- if series is empty

                                 false- if series is not empty'''




'''import pandas as pd

s=pd.Series([1,2,3,4],name="Numbers")


print(s)

print(s.index)#gives details on index like start index and stop index and step value

#if we want to change index

s=pd.Series([1,2,3,4],index=['a','b','c','d'],name="Numbers")


print(s)



#array

import pandas as pd

s=pd.Series([1,2,3,4],index=['a','b','c','d'],name="Numbers")
s.array

print(s.array)# display data in array format



#to get only vales

import pandas as pd

s=pd.Series([1,2,3,4],index=['a','b','c','d'],name="Numbers")

print(s.values)



# to get data type

import pandas as pd

s=pd.Series([1,2,3,4],index=['a','b','c','d'],name="Numbers")

print(s.dtypes)



s=pd.Series([1.2,2.3,3.4,4.5],index=['a','b','c','d'],name="Numbers")

print(s.dtypes)



#to get shape of series

import pandas as pd

s=pd.Series([1,2,3,4],index=['a','b','c','d'],name="Numbers")

print(s.shape)


#to display dimension

import pandas as pd

s=pd.Series([1,2,3,4],index=['a','b','c','d'],name="Numbers")

print(s.ndim)


#to display memory used by values

import pandas as pd

s=pd.Series([1,2,3,4],index=['a','b','c','d'],name="Numbers")

print(s.nbytes)




# to display memory used by values and index

import pandas as pd

s=pd.Series([1,2,3,4],index=['a','b','c','d'],name="Numbers")

print(s.memory_usage())


#if we want to know only memory used by values

import pandas as pd

s=pd.Series([1,2,3,4],index=['a','b','c','d'],name="Numbers")

print(s.memory_usage(index=False))


#to know the size


import pandas as pd

s=pd.Series([1,2,3,4],index=['a','b','c','d'],name="Numbers")

print(s.size)


# to know the name of series

import pandas as pd

s=pd.Series([1,2,3,4],index=['a','b','c','d'],name="Numbers")

print(s.name)


# to check empty or not

import pandas as pd

s=pd.Series([1,2,3,4],index=['a','b','c','d'],name="Numbers")

print(s.empty)

import pandas as pd

s1=pd.Series()

print(s1.empty)




#mathematical operation on series: add,sub,mul,div,mod,power,<,>,=


#adding of 2 series

import pandas as pd

#s1=pd.Series([1,2,3,4],index=['a','b','c','d'],name="Numbers")

#s2=pd.Series([5,6,7,8],index=['e','h','i','j'],name="Numbers1")


s1=pd.Series([1,2,3,4])

s2=pd.Series([6,7,8,1])

print(s1)
print(s2)

print(s1.add(s2))
print(s1+s2)


print(s1.sub(s2))

print(s1-s2)


print(s1.mul(s2))
print(s1*s2)

print(s1.div(s2))
print(s1/s2)

print(s1.mod(s2))
print(s1%s2)


print(s1.pow(s2))
print(s1**s2)


print(s1.le(s2))
print(s1<s2)


print(s1.gt(s2))
print(s1>s2)'''



import pandas as pd

s1=pd.Series([1,2,3,4])

s2=pd.Series([1,7,8,9])

print(s1.equals(s2))
print(s1==s2)











