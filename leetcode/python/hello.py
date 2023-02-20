'''s="Hi Noori"
print(s)
print("welcome to python filed")



#checking for odd or even
n=int(input("ENTER THE NUMBER:"))
if n%2==0:
      print("Given no. is even")
else:
    print("Given no. is odd")


#printing n number of even number
a=int(input("ENTER THE START NUMBER:"))
b=int(input("ENTER THE END NUMBER:"))
for n in range(a,b):
    if n%2==0:
        print(n)
    


#factorial of a given number using

n=int(input("ENTER THE NUMBER:"))
factorial=1
if n<0:
    print("no factorial for negative numbers")
elif n==0:
    print("factorial of 0 is 1")
else:
    for i in range(1,n+1):
        factorial=factorial*i
    print("Factprial of",n,"is",factorial)



#checking for positive or negative
n=float(input("enter number:"))
if n>0:
    print(n,"is positive")
elif n==0:
    print(n,"is zero")
else:
    print(n,"is negative")


#checking given number is prime or not
n=int(input("ENTER THE NUMBER:"))
if n>1:
    for i in range(2,n):
        if (n%i)==0:
            print(n,"is not a prime number")
            print(i,"times",n//i,"is",n)
            break
    else:
        print(n,"is prime number")
else:
    print(n,"is not a prime number")



#display all prime numbers in a given range

a=int(input("ENTER THE START NUMBER:"))
b=int(input("ENTER THE END NUMBER:"))
for i in range(a,b):
    if i>1:
        for j in range(2,i):
            if i%2==0:
                break
        else:
            print(i)'''



'''#finding given number is factorial or not

n=int(input("enter number:"))
def isfactorial(n):
    i=s=1
    if s<n:
        i=i+1
        s=s*i
    return s
    if s==n:
        print("true")
    else:
        print("false")'''
      

'''#reverse a string
def reverse(x):
    return x[::-1]
txt=reverse("hello")
print(txt)



##reverse using for loop
n=input("enter the number:")
for i in reversed(n):
    print(i,end="")


#calculator

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

def mod(x,y):
    return x%y

print("select operation.")
print("1:Add")
print("2:subtraction")
print("3:multiply")
print("4:divide")
print("5:mod")

while True:
    choice=input("enter choice:")
    if choice in('1','2','3','4','5'):
        n1=float(input("first number"))
        n2=float(input("second number"))
        if choice == "1":
            print(n1,"+",n2,"=",add(n1,n2))
        elif choice == "2":
            print(n1,"-",n2,"=",subtract(n1,n2))
        elif choice == "3":
            print(n1,"*",n2,"=",multiply(n1,n2))
        elif choice == "4":
            print(n1,"/",n2,"=",divide(n1,n2))
        elif choice == "5":
            print(n1,"%",n2,"=",subtract(n1,n2))
    else:
        print("out of range")
    nextcalculation=input("next calculation:")
    if nextcalculation =="no":
        break
    else:
        print("invalid input")'''


def switch():
    a=int(input("enter first value:"))
    b=int(input("enter second value:"))
    print("press 1 for addition\n press 2 for subtraction\n press 3 for multiplication \n press 4 for division\n press 5 for mod")

    choice = int(input("Select operation "))
    if choice ==1:
        result=a+b
        print("Addition:",result)
    elif choice ==2:
        result=a-b
        print("Subtraction:",result)

    elif choice ==3:
        result=a*b
        print("Multiolication:",result)

    elif choice ==4:
        result=a/b
        print("Division:",result)
    elif choice ==5:
        result=a%b
        print("mod:",result)
    else:
        print("Invalid value")


switch()















































