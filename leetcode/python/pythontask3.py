'''


#27.python code for Linear Serach


def lsearch(arr,ele):
    for i in range(len(arr)):
        if arr[i]==ele:
            return i
    return -1

arr=[1,2,45,23,34,78]
ele=23

print(lsearch(arr,ele))



#python code for Binary Serach


def bsearch(arr,low,high,ele):
    if high>=low:
        mid=(high+low)//2
        if arr[mid]==ele:
            return mid
        elif arr[mid]>ele:
            return bsearch(arr,low,mid-1,ele)
        else:
            return bsearch(arr,mid+1,high,ele)
    else:
        return -1

arr=[2,34,56,78,98]
ele=56
print(bsearch(arr,0,len(arr)-1,ele))




#28. Python code for all Sorting techniques


#bubble sort

def bubblesort(array):
    for i in range(len(array)-1):
        for j in range(0,len(array)-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    print(array)
data=[1,56,-3,7,9]
bubblesort(data)
#print(data)
    
print(len(data))



#selection sort

def selectionsort(array):
    for i in range(len(array)-1):
        minindex=i
        for j in range(i+1,len(array)):
            if array[j]<array[minindex]:
                minindex=j
        array[i],array[minindex]=array[minindex],array[i]
    print(array)
#array=[1,-5,23,45,34,78,75]
array=[int(array) for array in input("enter array elements:").split()]
selectionsort(array)



#29.Python program to Count Uppercase, Lowercase, special character and numeric values using Regex


s="SuhanaKhan_123@"
upper=0
lower=0
number=0
spl=0
#upper,lower,number,spl=0,0,0,0
for i in range(len(s)):
    if s[i]>='A' and s[i]<='Z': upper+=1
    elif s[i]>='a' and s[i]<='z': lower+=1
    elif s[i]>='0' and s[i]<='9': number+=1
    else: spl+=1


print(upper,lower,number,spl)



#30.Python Program to Remove duplicate words from Sentence

s=input("Enter sentence:")
l=s.split()
k=[]
for i in l:
    if i not in k:
        k.append(i)

print(' '.join(k))



#31.Python Regex | Program to accept string ending with alphanumeric character


import re

rexp='[a-zA-Z0-9]$'

def checkstring(s):
    if(re.search(rexp,s)):
        print("accepted")
    else:
        print("Not accepted")

s1="helloworld@"
s2="SnehaAgarwal"

print(checkstring(s1))
print(checkstring(s2))



#32.Categorize Password as Strong or Weak using Regex in Python
        

import re
def check(pwd):
    if pwd == "\n" or pwd == " ":
        return "Password must not contain a newline or space!"

    if 8 <= len(pwd) <= 15:
        if not re.search('[a-z]', pwd):
            `print("Weak Password! At least one lowercase alphabet should be present!")

        elif not re.search('[A-Z]', pwd):
            print("Weak Password! At least one uppercase alphabet should be present!")

        elif not re.search('[0-9]', pwd):
            print("Weak Password! At least one digit should be present!")

        elif not re.search('[_@$]', pwd):
            print("Weak Password! At least one special char should be present!")

        elif re.search(r'(.)\1\1\1', pwd):
            print("Weak Password! Char repetition more than 3 times!")

        elif re.search(r'(..)(.*?)\1', pwd):
            print("Weak Password! String pattern repetition!")

        else:
            print("The given password is a strong password!")

    else:
        print("Weak Password! Password must be 8 to 15 characters long! ")

ip_str = input("Enter the string: ")
check(ip_str)



#33.Python program to extract IP address from file


import socket
hostname=socket.gethostname()
ipaddress=socket.gethostbyname(hostname)
print(hostname)
print(ipaddress)



#34.Count number of lines in a text file in Python


with open(r"C:\Users\noori.zafar\Documents\python\basics3.txt",'r') as fp:
    nl=sum(1 for i in fp) #including empty lines
    #nl=sum(1 for i in fp if  i.rstrip())-->without empty line


    print("number of lines in a file is ",nl)

#35.Python Program to merge two files into a third file



print("Enter the Name of First File: ", end="")
fileOne = input()
print("Enter the Name of Second File: ", end="")
fileTwo = input()
print("Enter the Name of Third File: ", end="")
fileThree = input()
content = ""

fh = open(fileOne, "r")
for line in fh:
    content = content + line + '\n'
fh.close()
fh = open(fileTwo, "r")

for line in fh:
    content = content + line + '\n'
fh.close()
fh = open(fileThree, "w")
fh.write(content)

print("\nFile merged successfully!")'''



#

d=d1=""
with open(








