def reverseint(a):
    r=0
    while(a>0):
        n=a%10
        r=r*10+n
        a=a//10
    return r

a=1234
print("reverse of",a, " is:",reverseint(a))
