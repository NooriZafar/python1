

'''#Python Program for Changing Timezone

#import matplotlib

import matplotlib.pyplot as plt

country = ['A', 'B', 'C', 'D', 'E']
gdp_per_capita = [45000, 42000, 52000, 49000, 47000]

plt.bar(country, gdp_per_capita)
plt.title('Country Vs GDP Per Capita')
plt.xlabel('Country')
plt.ylabel('GDP Per Capita')
plt.show()


#4.Multiply all numbers in the list

l=[1,3,5,6,8]
mul = 1
for x in l:
    mul *= x
print(mul)


    
#5.Python program to find second largest number in a list
#5.1 using sort and displaying

l=[1,23,45,56,77]
l.sort()
print(l[-2])


#5.1 removing max and displayind second max
n1=[1,23,45,3,42]
nl=set(l)
nl.remove(max(nl))
print(max(nl))



#using for loop

first = l[0] 
second = l[0]   
for i in range(len(l)):  
    if l[i] > first:  
        first = l[i]  

 

for i in range(len(l)):  
    if l[i] > second and l[i] != first:  
        second = l[i]  
print(second)  


#6.Remove multiple elements from a list in Python

l=[2,3,6,"aliya",4,5,"Noori","sri"]
del l[1:3]
print(l)


l=[2,3,6,"aliya",4,5,"Noori","sri"]
newlist = []
for i in l:
    if i not in ('Noori', 5):
        newlist.append(i)
l = newlist
print(l)

 

l=[2,3,6,"aliya",4,5,"Noori","sri"]
remove = [6,"aliya",4]

final = list(set(l) - set(remove))
print(final)



#7.Python – Remove empty List from List

lst = [[1, 2, 3], [1, 2], [], [], [], [1, 2, 3, 4], [], []]

print([x for x in lst if x])
print([x for x in lst if x!=[]])




#8. Count occurrences of an element in a list


l = ["a", "ab", "a", "abc", "ab", "ab"]
k = {}
for j in l:
    if j in k:
        k[j] +=1
    else:
        k[j] =1
print(k)



#9.Python program to find Cumulative sum of a list


l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
cum_l=[]   
y = 0  
for x in range(0,len(l)):  
    y=y+l[x]  
    cum_l.append(y)
print("Given List", l)
print("Cumulative List", cum_l)



#10.Given two lists, sort the values of one list using the second list.


x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
y = [0,   1,   1,    0,   1,   2,   2,   0,   1]
zipped_pairs = zip(y, x)
z = [x for _, x in sorted(zipped_pairs)]
print(z)



x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
y = [0,   1,   1,    0,   1,   2,   2,   0,   1]
zipped_pairs = zip(y,x)

sorted_pairs = sorted(zipped_pairs)
print(sorted_pairs)


result = [item[1] for item in sorted_pairs]

print(result)




#11.Get Kth Column of Matrix

list= [[5, 6, 7],
       [9, 10, 2], 
       [10, 3, 4]]
print("The original list is : " + str(list))
K = 1
res = [sub[K] for sub in list]
print(res)




#14.Python – Convert Snake case to Pascal case

str = "suhana_khan"
print("The original string is : " + str)
res = str.replace("_", " ").title().replace(" ", "")
print("The String after changing case : " + res)



#15.Python – Words Frequency in String Shorthands


test_str = 'frequency of a word is simply the total number of times a word occurs in the string'
print("The original string is : " + str(test_str))

res = {key: test_str.count(key) for key in test_str.split()}
print("The words frequency : " + str(res)) 




#16.Python | Check if a Substring is Present in a Given String


string="HelloWorld"
sub='ellos'
if sub in string:
    print("present")
else:
    print("not found")


#input from user
    
string=input("Enter string:")
sub_str=input("Enter word")
if(string.find(sub_str)==-1):
      print("Substring not found in string")
else:
      print("Substring is present in string")



#17.Python program to accept the strings which contains all vowels




def CheckString(s):
    s = s.lower()
    vowels = set("aeiou")
    for char in s:
        if char in vowels:
            vowels.remove(char)
    if len(vowels) == 0:
        print("Accepted")
    else:
        print("Not accepted")
s= "aeiousda"
CheckString(s)



#18.Python | Count the Number of matching characters in a pair of string


def count(s1, s2):
    char_of_s1=set(s1)
    char_of_s2=set(s2)    
    common_char= char_of_s1 & char_of_s2 #intersection
    print("Matching Characters: ",len(common_char))
s1="noori"
s2="sridevi"
count(s1,s2)



#19. Maximum frequency character in String

test_str = "suhanakhan"

print ("The original string is : " + test_str)
all_freq = {}
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
res = max(all_freq, key = all_freq.get)
print (res)


#20.– Convert key-values list to flat dictionary


test_dict = {'month' : [1, 2, 3],
             'name' : ['Jan', 'Feb', 'March']}
print("The original dictionary is : " + str(test_dict))
res = dict(zip(test_dict['month'], test_dict['name']))
print("Flattened dictionary : " + str(res))




#21. Append Dictionary Keys and Values ( In order ) in dictionary


from itertools import chain

dic={"1":"Noori","3":"Ahad","2":"Hania"}
print(dict)

#print(dic.keys()+dic.values())#can't perform in dic

print(list(dic.keys())+list(dic.values()))


print(list(chain(dic.keys(),dic.values())))#before using chain we should import


a=list(dic.keys())
b=list(dic.values())
a.extend(b)
op=a
print("ordered keys and value:",op)



#22.Check order of character in string using OrderedDict( )


from collections import OrderedDict

def checkorder(string,patteren):
    dic=OrderedDict.fromkeys(string)
    start=0
    for key,value in dic.items():
        if(key==pattern[start]):
            start+=1
        if(start==(len(pattern))):
            return "True"
    return "False"
string="Hello Noori"
pattern="on"

print(checkorder(string,pattern))



#23.K’th Non-repeating Character in Python using List Comprehension and OrderedDict


from collections import OrderedDict

def kthrepeat(input,k):
    dict=OrderedDict.fromkeys(input,0)
    for i in input:
        dict[i]+=1
    nonrepeatdict=[key for (key,value) in dict.items() if value==1]
    if len(nonrepeatdict)<k:
        return "less"
    else:
        return nonrepeatdict[k-1]

    

if __name__=="__main__":

    input=" hello world"
    k=3
    print(kthrepeat(input,k))



#24.Python | Convert a list of Tuples into Dictionary


l=[("1","Noori"),("2","Ahad")]
d=dict(l)
print(d)


def convert(tup,dic):
    dic=dict(tup)
    return dic


tup=[("1","Noori"),("2","Ahad")]

dic={}
print(convert(tup,dic))




l=[("1","Noori"),("2","Ahad")]
dic=dict()
for key,value in l:
    dic.setdefault(key,[]).append(value)
print(dic)




#25.Counting the frequencies in a list using dictionary in Python

l=[1,1,2,3,4,1,3,2,1,4,3,1,6]
d={}
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for key,value in d.items():
    print(key,value)
print(d)


#
def countfrequency(l):
    d={}
    for i in l:
        d[i]=l.count(i)
    
    for key,value in d.items():
        print(key,value)


l=[1,1,2,3,4,1,3,2,1,4,3,1,6]
print(countfrequency(l))





#26.Python counter and dictionary intersection example (Make a string using deletion and rearrangement)
#Eg: Input : s1 = ABHISHEKsinGH
 #s2 = gfhfBHkooIHnfndSHEKsiAnG
#Output : Possible


from collections import Counter

def countdict(s1,s2):
    d1=Counter(s1)
    d2=Counter(s2)

    res=d1 & d2

    return res==d1

if __name__ == "__main__":
    s1 = "ABHISHEKsinGH"
    s2 = "gfhfBHkooIHnfndSHEKsiAnG"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 

    if countdict(s1,s2)==True:
        print("possible")
    else:
        print("Not Possible")





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
print(checkstring(s2))'''



#32.Categorize Password as Strong or Weak using Regex in Python
        

import re
def check(pwd):
    if pwd == "\n" or pwd == " ":
        return "Password must not contain a newline or space!"

    if 8 <= len(pwd) <= 15:
        if not re.search('[a-z]', pwd):
            print("Weak Password! At least one lowercase alphabet should be present!")
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



































