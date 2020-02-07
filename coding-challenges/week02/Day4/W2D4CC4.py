# 4) Write a Python function that takes a number as a parameter and check the number is prime or not

from math import sqrt

input_num=int(input('enter a number to find out, if it is prime or not: '))
if input_num==2 or input_num==3:
    print(input_num,'is a prime')
elif input_num>3:
    i=2
    while i<=int(sqrt(input_num)):
        if input_num%i==0:
            print('the given number is not a prime')
            break
        i+=1
    else:
        print('the given number is a prime')  

else:
    print(' 1 is neither prime nor composite')

