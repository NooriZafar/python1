
'''
#adding of two matrix

X = [[1,2,3],  
       [4,5,6],  
       [7,8,9]]  
  
Y = [[10,11,12],  
       [13,14,15],  
       [16,17,18]]  
  
result = [[0,0,0],  
                [0,0,0],  
                [0,0,0]]

# iterate through rows  
for i in range(len(X)):  
   # iterate through columns  
   for j in range(len(X[0])):  
       result[i][j] = X[i][j] + Y[i][j]


#result = [[X[i][j] + Y[i][j]  for j in range(len(X[0]))] for i in range(len(X))]

       
for r in result:  
   print(r)  


print(range(len(X)))
print(range(len(X[0])))


#multiply of two matrix

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)





#


class person(object):
   def __init__(self,name,id):
      self.name=name
      self.id=id
   def display(self):
      print(self.name)
      print(self.id)
   def details(self):
      print("My name is {}".format(self.name))
      print("Id:{}".format(self.id))
class Employee(person):
   def __init__(self,name,id,salary,post):
      self.salary=salary
      self.post=post
      person.__init__(self,name,id)
   def details(self):
      print("My name is {}".format(self.name))
      print("Id:{}".format(self.id))
      print("post:{}".format(self.post))
a=Employee('Noori',12,60000,"Developer")
a.display()
a.details()



#checking string palindrone or not 

n=input("enter word:")

if n==n[::-1]:
   print("palindrome")
else:
   print("Not palindrome")




#cheching number palindrome or not

n=int(input("enter :"))
temp=n
sum=0
while temp>0:
    r=temp%10
    sum=sum*10+r
    temp=temp//10
if n==sum:
    print("palindrome")
else:
    print("not palindrome")




#count the number of each vowel


vowels='aeiou'

input="hi, where are you from?"

input=input.casefold()

count={}.fromkeys(vowels,0)

for char in input:
   if char in count:
      count[char]+=1
print(count)


#iterate through 2 list in paraLLEL

l1=[1,2,3,4]
l2=[5,6,7,8]
for i,j in zip(l1,l2):
   print(i,j)


#display calender

import calender
y=int(input("Enter year:"))

m=int(input("Enter month:"))

print(calender.month(y,m))


#print duplicate elements in array


arr=[1,2,3,1,5,6,5,7,8,3]

for i in range(0,len(arr)):
   for j in range(i+1,len(arr)):
      if (arr[i]==arr[j]):
         print("repeatedelements :",arr[i])


      
#copy one elements of array in another


arr=[1,2,3,4,5]
print(arr)
arr2=[None]*len(arr)

for i in range(len(arr)):
   arr2[i]=arr[i]
   print(arr2[i])'''



#array elements in reverse order


a=[1,2,3,4,5]


print("original array:")

for i in range(0,len(a)):
   print(a[i])

print("array in reverse:")

for i in range(len(a)-1,-1,-1):
   print(a[i])



#find max element in array


arr=[23,45,34,12,99]

max=arr[0]

for i in range(0,len(arr)):
   if(arr[i]>max):  #arr[i]<min for smallest element
      max=arr[i]

print("largest element in array:",max)




# sorting array in ascending order

a=[8,7,3,2,6]
temp=0


print("original elements:")
for i in range(len(a)):
   print(a[i],end="")


for i in range(len(a)):
   for j in range(i+1,len(a)):
      if(a[i]>a[j]):
         a[i],a[j]=a[j],a[i]

#print()

print("Sorted array:")

for i in range(len(arr)):
   print(a[i],end="")



















