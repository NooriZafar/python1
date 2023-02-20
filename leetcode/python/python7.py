
''''

def print_rangoli(size):
    #n=size
    l=list(map(chr,range(97,123)))
    x=l[n-1::-1]+l[1:n]
    m=len("-".join(x))
    for i in range(1,n):
        print('-'.join(l[n-1:n-i:-1]+l[n-i:n]).center(m,'-'))
    for i in range(n,0,-1):
        print('-'.join(l[n-1:n-i:-1]+l[n-i:n]).center(m,"-"))



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)






#display number in decimal,octal,hexa,binary


def print_formatted(number):
    width = len(str(bin(number)[2:]))
    for num in range(1, number + 1):
        d = str(num)
        o = str(oct(num))[2:]
        h = str(hex(num))[2:].upper() 
        b = str(bin(num))[2:]
        print(f"{d.rjust(width)} {o.rjust(width)} {h.rjust(width)} {b.rjust(width)}")
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)





def print_formatted(number):
    for i in range(1, number + 1):
        width = number.bit_length()
        print(f'{i:{width}} {i:{width}o} {i:{width}X} {i:{width}b}')
    return None
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)





#to display starting letters in capital



def solve(s):
    for i in s.split():
        s=s.replace(i,i.capitalize())
    return s


if __name__ == '__main__':

    s = input()
    result = solve(s)

    print(result)




#max element and its length

def longestlength(a):
    max1= len(a[0])	
    temp= a[0]	
    for i in a:
        if (len(i) > max1):
            max1 = len(i)
            temp=i
            print("The word with longest length is:", temp ,"and length is", max1)
a=['noori','aliya','pavi']
longestlength(a)'''	



#count all letters,digits,special synbols from a given string

def find_digits_chars_symbols(string):
    char_count=0
    digit_count=0
    symbol_count=0
    for char in string:
        if char.isalpha():
            char_count +=1
        elif char.isdigit():
            digit_count +=1
        else:
            symbol_count +=1
    print("characters:",char_count,"digits:",digit_count,"symbol:",symbol_count)
string="P%yjm*789$"
print("total count of  characters,digits and symbols \n")
find_digits_chars_symbols(string)








