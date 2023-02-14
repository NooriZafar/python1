def longestsubstring(s):
    if len(set(s))==len(s):
        return len(s)
    substring=''
    maxlen=1
    for i in s:
        if i not in substring:
            substring+=i
            maxlen=max(maxlen,len(substring))
        else:
            substring=substring.split(i)[1]+i
    return maxlen

s="hieehelso"
print(longestsubstring(s))           
