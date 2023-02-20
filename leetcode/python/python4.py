'''
# to check given positive number is power of 2

n=int(input("Enter the nymber:"))
if n>0 and (n&(n-1))==0:
    print(n,"is power of 2")
else:
    print(n,"is not power of 2")

# to check given positive integer is power of 3


n=int(input("Enter the nymber:"))
def is_power_of_three(n):
    while (n%3==0):
        n/=3;
    return n==1;
print(is_power_of_three(n))



#if a given number is 123 then display as 123,12,1


n=input("Enter the nymber:")
for i in range(len(n)):
    print(n[i:])




#reading list of integers from user

list=[int(i) for i in input("enter list elements").split()]  we can give any range 
list1=[int(i) for i in input("enter list elements")]  # we can give only single digit integer

print(list)    #i/p:1234  o/p:[1234]
print(list1)   #i/p:1234  o/p:[1,2,3,4]



#to find max element

list1=[int(i) for i in input("enter list elements").split()]
print(list1)
print(max(list1))


#print sum of all given number
l=[12,3,4,56,7,9]
count=0
for i in l:
    count+=i
print(count)


#one more method for sum of digitd
l=[12,3,4,56,7,9]
print(sum(l))


print(sum(range(1,12,2))) #to print sum of alternative numbers


#break out a number into multiple numbers

n=int(input("enter the nymber:"))
s=[int(i) for i in str(n)]  #o/p:[1,2,3]
s=[i for i in str(n)]       #o/p:['1','2','3']
print(s)



#another method to break out a number into multiple numbers

n=int(input("enter the nymber:"))
s=[]
while n:
    s.append(n%10)
    n//=10
print(s)
s.reverse()
print(s)



#to find no. of occurrence of character/number

count=0
string="helloworld"
checkchar="o"
for i in string:
    if i==checkchar:
        count+=1
print(count)

#print(string.count(checkchar))-->checks in one line for above code


#compute all the permutation of a string

def permutation(string,i=0):
    if i==len(string):
        print("".join(string))
    for j in range(i,len(string)):
        words=[c for c in string]
        permutation(words,i+1)
print(permutation('yup'))



from itertools import permutations
words=["".join(p) for p in permutations('pro')]
print(words)



#sort in alphabetical order
string="Hello Sneha, How are you"
words=[i.lower() for i in string.split()]
words.sort()

print("sorted list is:")
for i in words:
    print(i)



#interchange first and last letter

def swaplist(list):
    size=len(list)
    list[0],list[size-1]=list[size-1],list[0]
    return list
list=[1,2,3,4]
print(swaplist(list))'''


#smallest element in lis

l=[11,2,5,67]
l.sort()
print(l[-2]) #second largest number
print(min(l))  #smallest number
print(max(l))  #largest number






















































