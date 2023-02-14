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
