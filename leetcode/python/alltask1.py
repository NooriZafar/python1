'''#longest common prefix
s=['aa','aaa','aad','aaf','aaaf']
def commonprefix(s):
    s.sort()
    i=0
    first,last=s[0],s[-1]
    while i<len(first) and i<len(last):
        if first[i]!= last[i]:
            break
        i+=1
    return first[0:i]

print(commonprefix(s))



#remove nth node from end of the list

def removenthfromlast(head,n):
    temp=dummy=head
    count=0
    if head.next==None:
        return None
    while head.next!=None:
        count+=1
        if count>n:
            dummy=dummy.next
        head=head.next
    if count+1!=n:
        dummy.next=dummy.next.next
    return temp

s=[1,2,3,4,8,6]
d=2

print(removenthfromlast(d,s))


#max sub array in python

arr=[1,2,3,4,-5]
def maxsubarray(arr):
    dp=[0 for i in range(len(arr))]
    dp[0]=arr[0]
    for i in range(1,len(arr)):
        dp[i]=max(dp[i-1]+arr[i],arr[i])
    return max(dp)
print(maxsubarray(arr))'''



def reverseList(list):
    prev=None
    first=list
    while first:
        tmp=first.next
        first.next=prev

        first=second
        if second:
            second=second.next
    list.head=prev

list=[1,2,3,4,5]
print(reverseList(list))



























    
    
