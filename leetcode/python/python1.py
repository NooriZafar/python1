'''#leap year

n=int(input("Enter the year:"))
if n%400==0 and n%100==0:
    print(n,"is leap year")
elif n%4==0 and n%100!=0:
    print(n,"ia a leap year")
else:
    print(n,"is not a leap year")
    


# progrm to find simple interest:si=(p*t*r)/100

def simpleinterest(p,t,r):
    si=(p*t*r)/100
    print("simple interest is:",si)
    return si
simpleinterest(8,6,8)
#p=int(input("enter principal:"))
#t=int(input("enter time period:"))
#r=int(input("enter rate of interest:"))




#to check for amstrong number .ex:153=(1*1*1+5*5*5+3*3*3)

n=int(input("Enter number:"))
temp=n
sum=0
while temp>0:
    r=temp%10
    sum``````````````````=sum+(r**3)
    temp=temp//10
if num==sum:
    print("amstrong")
else:
    print("not amstrong")

    


#multiplication table
n=int(input("enter number:"))
for i in range(1,11):
    print(n,'*',i,'=',n*i)

    


#sum of natural number upto n


n=int(input("Enter number:"))
if n<0:
    print("enter a positive number")
else:
    sum=0
    for i in range(n+1):
        sum=sum+i
    print(sum)

    


#binary,decimal,hexa

n=int(input("Enter number:"))
print("decimal value of",n,"is:")
print(bin(n),"in binary.")
print(oct(n),"in octal.")
print(hex(n),"in hexadecimal")




#pattern program

n=int(input("enter n:"))

for i in range(1,n):
   for j in range(1,i+1):
       print(j,end=" ")
   print("\n")
   


#print number of vowels and consonent

n=input("Enter text:")
vowel = 0	
consonent = 0
whitespace=0
for i in n:	
    if i in "aeiou":
        vowel += 1
    elif i ==' ':
        whitespace+=1
    else:
        consonent += 1	
print("vowels:",vowel)	
print("consonent:",consonent)	
print("whitespace:",whitespace)



#Sorting a list without using sort method

List=[2,1,32,23,45,54]
for i in range(0,len(List)):
    for j in range(i+1,len(List)):
        if List[i] >=List[j]:
            List[i],List[j] = List[j],List[i]
print(List)'''




#Removing Negative element in list using List comphension

list=[int(i) for i in input("enter array elements:").split()]
remove = [i for i in list if i>0]	
print(remove)




























    
