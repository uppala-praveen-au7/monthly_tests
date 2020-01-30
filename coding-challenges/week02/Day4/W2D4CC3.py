# 3) Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

count_small=0
count_cap=0
count_oth=0

stryng=input('please enter a word to calculate the number of capital letters and small letters in it: ')
for i in range(0, len(stryng)):
    if ord(stryng[i]) in range(ord('A'),ord('Z')+1):
        count_cap+=1
    elif ord(stryng[i]) in range(ord('a'),ord('z')+1):
        count_small+=1
    else:
        count_oth+=1
print('Number of capital letters in the given input is: ', count_cap)
print('Number of small letters in the given input is: ', count_small)
print('Number of other characters in the given input is: ', count_oth)
