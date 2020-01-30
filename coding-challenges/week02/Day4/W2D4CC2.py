# 2) Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). 
# Print average and product of all numbers.

# print(ord('q'))= 113

sum_1=0
product_1=1
count=0
dummy=0
while dummy>=0:
    var_input=input('Enter an integer to continue or \'q\' to quit:')
    if var_input!='q':
        sum_1+=int(var_input)
        product_1*=int(var_input)
        dummy+=1
        continue
    else:
        print('Average of the given integers: ',(sum_1/dummy))
        print('product of the given integers: ',product_1)
        break
        
