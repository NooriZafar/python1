
'''
#36.Python program to read file word by word

s=input("Enter data:")

l=s.split()

for i in range(len(l)):
    print(l[i])
    #print(i)

    

#
with open('python3.py','r') as f:
    for line in f:
        for word in line.split():
            print(word)
            


#37.Python Program to Reverse the Content of a File using Stack

class Stack:
      
    def __init__(self):
          
        # Creating an empty stack
        self.arr = []
          
    # Creating push() method.
    def push(self, val):
        self.arr.append(val)
   
    def is_empty(self):
          
        # Returns True if empty
        return len(self.arr) == 0
  
    # Creating Pop method.
    def pop(self):
          
        if self.is_empty():
            print("Stack is empty")
            return
          
        return self.arr.pop()
  
def reverse_file(filename):
       
    S = Stack()
    original = open(filename)
      
    for line in original:
        S.push(line.rstrip("\n"))
      
    original.close()
       
       
    output = open(filename, 'w')
      
    while not S.is_empty():
        output.write(S.pop()+"\n")
      
    output.close()
  
  
# Driver Code
filename = "samplefile.txt"
  
# Calling the reverse_file function
reverse_file(filename)
   
# Now reading the content of the file
with open(filename) as file:
        for f in file.readlines():
            print(f, end ="")



#38.Python program to reverse the content of a file and store it in another file


f2 = open("empty.txt", "w")
  
with open("samplefile.txt", "r") as f:
    data = f.readlines()

data1 = data[::-1]

f2.writelines(data1)
  
f2.close()



#39.Python Program to Reverse a linked list


#Python Program for Maximum height when coins are arranged in a triangle


def triangle(input1):
	if input1 < 1:
		return 'Zero'
	else:
		# Counter for controlling the coins in a row
		a = 1	
		height = 0
		while input1 > 0:
			if input1 - a >= 0:
				input1 = input1 - a
				a = a + 1
				height = height + 1
			else:
				break
		return height


if __name__ == "__main__":
	testinput1 = 22
	print(triangle(testinput1))'''



#Python Program for Program to Print Matrix in Z form



arr  = [[5, 19, 8, 7],
                   [4, 1, 14, 8],
                   [2, 20, 1, 9],
                   [1, 2, 55, 4]]


n=len(arr[0])
i=0
for j in range(0,n-1):
    print(arr[i][j],end=' ')
k=1
for i in range(0,n):
    for j in range(n,0,-1):
        if(j==n-k):
            print(arr[i][j],end=' ')
            break
    k+=1
i=n-1
for j in range(0,n):
    print(arr[i][j],end=' ')

























