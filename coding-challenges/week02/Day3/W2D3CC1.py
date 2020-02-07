# 1) Using range and for loop, print all multiples of 5, 7, 11 from 1 to 1001 


print("Multiples of 5")
for i in range(0,1002):
    if i%5==0:
        print(i)

print("Multiples of 7")
for i in range(0,1002):
    if i%7==0:
        print(i)

print("Multiples of 11")
for i in range(0,1002):
    if i%11==0:
        print(i)

print("Multiples of 5,7 and 11 ")
for i in range(0,1002):
    if i%5==0:
        if i%7==0:
            if i%11==0:
                print(i)
            else:
                continue