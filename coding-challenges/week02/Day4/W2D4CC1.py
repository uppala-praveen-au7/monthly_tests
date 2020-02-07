# 1) Write a program to find greatest common divisor (GCD) or highest common factor (HCF) of given two numbers.

# program is to find the lcm and fcf of two user defined integers

def hcf_func(first_num,second_num):
    dummy=0
    while dummy==0:
        if first_num>=second_num:
            next_div=first_num%second_num
            if next_div==0:
                if second_num==1:
                    print('Both the given numbers are co-prime numbers')
                else:
                    print('HCF of the given numbers is: ', second_num)

                return_var=second_num
                break
            else:
                second_num=first_num
                first_num=next_div
                continue
        else:
            next_div=second_num%first_num
            if next_div==0:
                if first_num==1:
                    print('Both the given numbers are co-prime numbers')
                else:
                    print('HCF of the given numbers is: ',first_num)

                return_var=first_num
                break
            else:
                first_num=second_num
                second_num=next_div
                continue
    return return_var

first_num=int(input('enter the first integer: '))
second_num=int(input('enter the second integer: '))
least_com_mul=(first_num*second_num)/(hcf_func(first_num,second_num))

print('LCM of the given numbers is: ', least_com_mul)

