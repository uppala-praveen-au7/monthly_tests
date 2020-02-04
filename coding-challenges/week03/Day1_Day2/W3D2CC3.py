# 3) Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

s=input('enter a string: ')
d={}
for i in range(len(s)):
    count=1
    for j in range(i+1,len(s)):
        if s[i]==s[j]:
            count+=1
            d[i]=count
            continue
        else:
            d[s[i]]=count
            continue
print(d)
