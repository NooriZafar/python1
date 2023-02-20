'''
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









    
    
 
