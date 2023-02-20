'''#bubble sort:it swap the adjacent elements if they are in wrong order.

def bubblesort(array):
    for i in range(len(array)-1):
        for j in range(0,len(array)-i-1):
            if array[j]>array[j+1]:
                ''''''temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp''''''
                array[j],array[j+1]=array[j+1],array[j]
    print(array)
data=[1,56,-3,7,9]
bubblesort(data)
#print(data)
    
print(len(data))'''



'''#selection sort:it selects min element from unsorted and put it at the beginning

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
#print(array)'''


'''#to merge 2 lists and sort it

a=[]
c=[]
n1=int(input("enter number of elements:"))
for i in range(n1):
    b=int(input("enter elements:"))
    a.append(b)
n2=int(input("enter number of elements:"))
for i in range(n2):
    d=int(input("enter elements:"))
    c.append(d)
new=a+c
new.sort()
print("before sort:",a+c)
print("sorted list is:",new)'''

#merge sort

def mergesort(array):
    #print("splitting",array)
    if len(array)>1:
        mid=len(array)//2
        lefthalf=array[:mid]
        righthalf=array[mid:]
        mergesort(lefthalf)
        mergesort(righthalf)
        i=j=k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                array[k]=lefthalf[i]
                i=i+1
            else:
                array[k]=righthalf[j]
                j=j+1
            k=k+1
        while i<len(lefthalf):
            array[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j<len(righthalf):
            array[k]=righthalf[j]
            j=j+1
            k=k+1
    print("merge",array)

array=[23,-5,45,3,67]
mergesort(array)
print(array)
            
    




  
