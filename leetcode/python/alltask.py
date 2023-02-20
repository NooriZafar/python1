
'''
#python progrom to swap first nd last element

l=[1,2,3,4,5]
n=len(l)
l[0],l[n-1]=l[n-1],l[0]
print(l)


def swap(l):
    n=len(l)
    l[0],l[n-1]=l[n-1],l[0]
    print(l)


l=[1,2,3,4,5]
swap(l)


#python program to swap 2 elements

def swaptwo(l):
    l[0],l[2]=l[2],l[0]
    print(l)

l=[23,45,67,76,80]
swaptwo(l)


#max of two numbres

def max(a,b):
    if a>b:
        print(a,"is max element")
    else:
        print(b,"is max element")
max(4,3)


maximum=max(2,6)
print(maximum)


#check for palindrome
s=12332
r=0
tem=s
while(s>0):
    n=s%10
    r=r*10+n
    s=s//10
print(r)
if tem==r:
    print("palindrome")
else:
    print("not an pallindrome")



#checks for duplicate

def checkduplicate(s):
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i]==s[j]:
                return True
    return False


#s="This is Noori"
s="hi sumya"
if checkduplicate(s):
    print("It contain duplicate")
else:
    print("Unique character")



def maxprofit(price,start,end):
    if(end<=start):
        return 0
    profit=0
    for i in range(start,end):
        for j in range(i+1,end+1):
            if price[j]>price[i]:
                curprofit=price[j]-price[i]+maxprofit(price,start,i-1)+maxprofit(price,j+1,end)
                profit=max(profit,curprofit)
    return profit

if __name__=='__main__':
    price=[90,170,250,300,30,525,685]
    n=len(price)
    print(maxprofit(price,0,n-1))


#add total 
l=12345
s=str(l)
sum=s[0]+s[-1]
print(sum)


#display num divisible by 7 and not by 5

l=[]
for i in range(1,100):
    if i%7==0 and i%5!=0:
        l.append(str(i))
print(','.join(l))



#to count numbers of letters and numbers

s=input()
d={"digit":0,"letters":0}
for i in s:
    if i.isdigit():
        d["digit"]+=1
    elif i.isalpha():
        d["letters"]+=1
    else:
        pass
print("letters",d["letters"])
print("digits",d["digit"])


#print prine numbers

n=int(input("Enter range:"))
for i in range(2,n):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)

#

def longestsubstring(s):
    if len(set(s))==len(s):
        return len(s)
    substring=''
    maxlen=1
    for i in s:
        if i not in substring:
            substring+=i
            maxlen=max(maxlen,len(substring))
        else:
            substring=substring.split(i)[1]+i
    return maxlen

s="hieehelso"
print(longestsubstring(s))       

#median of two sorted arrays

import heapq
import numpy as np

l1=[1,3]
l2=[2]
s=heapq.merge(l1,l2)
l=list(s)
print(l)


def findmedian(a,n):
    if n%2==0:
        z=n//2
        result=(a[z]+a[z-1])/2
        return result
    else:
        z=n//2
        result=a[z]
        return result
if __name__=='__main__':
    a1=[1,3]
    a2=[2,5]
    a3=a1+a2
    a3.sort()
    print("the median of two sorted array:",findmedian(a3,len(a3)))



#longest palindrome substring

def longestPalindrome(s):
    if (s==s[::-1]):
        return s
    else:
        return max([longestPalindrome(s[1:]),longestPalindrome(s[:-1])],key=len)

s="hibabab"

print(longestPalindrome(s))


#count number of nonempty substring

def countnonemptysubstring(s):
    n=len(s)
    return (n*(n+1)/2)
s=input()
print(countnonemptysubstring(s))


#reverse integer

def reverseint(a):
    r=0
    while(a>0):
        n=a%10
        r=r*10+n
        a=a//10
    return r

a=1234
print("reverse of",a, " is:",reverseint(a))


#string to int

a='10'
print(type(a))
b=int(a)
print(type(b))

import re
txt="This is noori"
x=re.search("This",txt)
if x:
    print("yes, we have a match")
else:
    print("no match")

#return number of times pattern occurs

import re
txt="This is noori"
x=re.findall("is",txt)
print(x)

#split the list

import re
txt="This is noori"
x=re.split("\s",txt)
print(x)'''






