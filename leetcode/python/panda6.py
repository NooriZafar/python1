


'''#converting dict to Dataframe

import pandas as pd

d={'name':['Noori','Ahad','Moin'],'age':[22,1,24]}
df=pd.DataFrame(d)

print(df)'''

'''l = ["a", "ab", "a", "abc", "ab", "ab"]
k = {}
for j in l:
    if j in k:
        k[j] +=1
    else:
        k[j] =1
print(k)

l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
cum_l=[]   
y = 0  
for i in range(len(l)):  
    y=y+l[i]  
    cum_l.append(y)
print("Given List", l)
print("Cumulative List", cum_l)


x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
y = [0,   1,   1,    0,   1,   2,   2,   0,   1]
zipped_pairs = zip(y,x)

sorted_pairs = sorted(zipped_pairs)
print(sorted_pairs)

result = [item[1] for item in sorted_pairs]
print(result)

test_str = 'frequency of a word is simply the total number of times a word occurs in the string'
print("The original string is : " + str(test_str))

res = {key: test_str.count(key) for key in test_str.split()}
print("The words frequency : " + str(res)) 




def count(s1, s2):
    char_of_s1=set(s1)
    char_of_s2=set(s2)    
    common_char= char_of_s1 & char_of_s2 #intersection
    print("Matching Characters: ",len(common_char))
s1="noori"
s2="sridevi"
count(s1,s2)


def pal(s):
    s1=s[::-1]
    if s1==s:
        print("pal")
    else:
        print("no")
pal("madams")


string="Hello Sneha, How are you"
words=[i.lower() for i in string.split()]
words.sort()

print("sorted list is:")
for i in words:
    print(i)'''



test_str = "suhanakhan"

print ("The original string is : " + test_str)
all_freq = {}
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
res = max(all_freq, key = all_freq.get)
print(res)















