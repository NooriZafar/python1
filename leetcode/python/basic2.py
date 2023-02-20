-----------------------
python dictionaries:

----------------------
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

Ex:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)--->{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
-----
11111.access item:

1.print(thisdict["brand"])--->Ford

2.print(thisdict.get("brand"))-->Ford
print(thisdict.keys())-->dict_keys(['brand', 'model', 'year'])
----
dict() Constructor:
            It is also possible to use the dict() constructor to make a dictionary.

Ex:

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)--->{'name': 'John', 'age': 36, 'country': 'Norway'}

------
-->adding new item:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change-->dict_keys(['brand', 'model', 'year'])

car["color"] = "white"

print(x) #after the change-->dict_keys(['brand', 'model', 'year', 'color'])

-------

-->Make a change in the original dictionary:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change-->dict_values(['Ford', 'Mustang', 1964])

car["year"] = 2020

print(x) #after the change-->dict_values(['Ford', 'Mustang', 2020])

--------
Get Items:
The items() method will return each item in a dictionary, as tuples in a list.

Ex:
x = thisdict.items()

------
Check if Key Exists:

Ex:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


2222.Change value:   thisdict["year"] = 2018
     update value:   thisdict.update({"year": 2020})

3333.pop:The popitem() method removes the last inserted item 

ex:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)-->{'brand': 'Ford', 'model': 'Mustang'}

4444.del:The del keyword removes the item with the specified key name and can
also delete complete dictionary

ex:

del thisdict["model"]
print(thisdict)-->{'brand': 'Ford','year': 1964}
--
del thisdict-->delete complete dict

5555> clear:clear() method empties the dictionary

Ex:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)-->{}

-----
loop:

ex
for x in thisdict:
  print(x)

o/p:
Ford
Mustang
1964

for x in thisdict:
  print(thisdict[x])

ö/p:
Ford
Mustang
1964

for x, y in thisdict.items():
  print(x, y)
o/p:

brand Ford
model Mustang
year 1964

6666:copy dict:

mydict = thisdict.copy()
print(mydict)
--
mydict = dict(thisdict)
print(mydict)

7777.nested dict:


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)-->{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}

another way:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)-->{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}
---
dictionary methods:
---

clear()		Removes all the elements from the dictionary
copy()		Returns a copy of the dictionary
fromkeys()		Returns a dictionary with the specified keys and value
get()			Returns the value of the specified key
items()		Returns a list containing a tuple for each key value pair
keys()		Returns a list containing the dictionary's keys
pop()			Removes the element with the specified key
popitem()		Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()		Updates the dictionary with the specified key-value pairs
values()		Returns a list of all the values in the dictionary

__________________________________________________________________________________

------------
if statement:(if,if else, if else if)
--------------

if condition:
	print(stmt1)
elif condition:
	print(stmt2)
else:
	print(none)

short hand(if,if else,if else with condition):

if a > b: print("a is greater than b")

print("A") if a > b else print("B")

print("A") if a > b else print("=") if a == b else print("B")

pass::::
if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

ex:
if b > a:
  pass

_______________________________________________________________________________________________

---------------
while loop:

-------------------

With the while loop we can execute a set of statements as long as a condition is true.

ex:
i = 1
while i < 6:
  print(i)             #With the break statement we can stop the loop even if the while condition is true
  if i == 3:
    break
  i += 1

ouput:
1
2
3
-----
i = 0
while i < 6:
  i += 1
  if i == 3:          #With the continue statement we can stop the current iteration, and continue with the next
    continue
  print(i)

output:
1
2
4
5
6

________________________________________________________________________________

----
for loop
-----------
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

output:

apple
banana

____________________________________________________________________________________________

-------------------
Creating a Function:
-------------------
In Python a function is defined using the def keyword

Ex:

def my_function():
  print("Hello from a function")

-----
Calling a Function: To call a function, use the function name followed by parenthesis.

ex:
def my_function():
  print("Hello from a function")

my_function()

-----
Arguments:

Information can be passed into functions as arguments.Arguments are specified after the function name, 
inside the parentheses. You can add as many arguments as you want,
 just separate them with a comma.

Ex:

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
---

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")-->Emil Refsnes
-----

Arbitrary Arguments, *args:

If you do not know how many arguments that will be passed into your function, 
add a * before the parameter name in the function definition.

Ex:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")-->The youngest child is Linus

----

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

output:
Recursion Example Results
1
3
6
10
15
21

______________________________________________________________________________________
-----
Python Lambda:
--------------

A lambda function can take any number of arguments, but can only have one expression.

ex:
x = lambda a : a + 10
print(x(5))-->15
---
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))-->13
----
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))-->22
------
_________________________________________________________________________
---------------------
array method
--------------------

append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()		Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list


_______________________________________________________________________________