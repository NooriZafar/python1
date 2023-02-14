import re
txt="This is noori"
x=re.search("This",txt)
if x:
    print("yes, we have a match")
else:
    print("no match")

#to print number of times the pattern accors

import re
txt="This is noori"
x=re.findall("is",txt)
print(x) #o/p:['is', 'is']

#to split the list
import re
txt="This is noori"
x=re.split("\s",txt)
print(x)
