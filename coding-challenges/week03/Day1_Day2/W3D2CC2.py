# 2) Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
n=int(input('enter a number: '))
d={}
for i in range(n+1):
     d[i]=i**2
print(d)
# print(list(map(lambda i:d[i]=i**2, i in range(0,n+1))))
