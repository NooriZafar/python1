''''
#covet upper to lower and lower to upper:swapcase

def swap_case(s):
    a=s.swapcase()
    return  a

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


#You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

def split_and_join(line):
    a=line.split(" ")
    a="-".join(a)
    return a
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


#read them and print 

def print_full_name(first, last):
    # Write your code here
    print("Hello "+first+' '+ last+"! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)



#print the number of times that the substring occurs in the given string. 

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string.startswith(sub_string, i):
            count+=1
    return count
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)





#To chech whether given string contain any alphanumeric,alpha,digit,upper,lower


#if __name__ == '__main__':
s = input()
print (any(char.isalnum() for char in s))

print(any(char.isalpha() for char in s))
    
print(any(char.isdigit() for char in s))

print(any(char.islower() for char in s))

print(any(char.isupper() for char in s))'''




thickness = int(input()) #This must be an odd number
c = 'N'

#Top Cone

for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
    
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
    
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
    
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
    
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
        


















