# 1) Write a Python program to iterate over dictionaries using for loops.

d={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9}
print('\n')
print(d.keys(),'\n')
print([i for i in d],'\n')
print(*[i for i in d],'\n')
print(d.values(),'\n')
print([i for i in d.values()],'\n')
print(*list(i for i in d.values()),'\n')
print(d.items(),'\n')
print([i for i in d.items()],'\n')
print([(i,j) for i,j in d.items()],'\n')
print(*[i for i in d.items()],'\n')
for i,j in d.items():
    print(i,j, end=' ')
print('\n')