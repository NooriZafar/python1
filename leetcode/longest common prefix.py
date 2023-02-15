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
