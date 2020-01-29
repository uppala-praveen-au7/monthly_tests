
# Taking an input from user
n=int(input('enter an integer, which is greeater than 0 and less than 27: '))
# Defining a list of alphabets
list =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# a finite loop to print the first n lines of the rangoli
# Here 'a' in the for loops is specifically used for the line in rangoli
# n is the maximum no of alphabet to be printed
# throughout the program 'i' is used as a dummy variable 
for a in range(0,n):
# printing the "-" before the alphabets by string concatenation
    print("-"*(2*n-2*a-2), end="")
# Printing alphabet at position n-i-1
# implies initially higher alphabets are printed 
# when i increases the lower alphabets will gets printed
# we used end="" in print function so that we can stay in
# the same line even after printing

    for i in range(0,a+1):
        print(list[n-i-1], end="")
# Here we used conditional statement to check
# the cursor is at what positin and in which line
# and then accordingly it will print "-" after the alphabet
# suppose, if the program prints alphabet on first line
# then it should not print hyphen after that since other part of the code
# take care of that and in anyother line the hyphen will only gets printed
# when the line value 'a' is greater than the position (dummy value) 'i'
        if a!=0 and a>i:
            print("-",end="")
# At the end of each iteration the dummy variable is reset to '0'
#  which wnables us to print the highest alphabet at the beginning of each line
        i=0

# This section completes right half of the upper n lines of rangoli
# Here we have to print "-" before each alphabet that's why the 
# the "-" part of the code is written before the alphabet part of the code
 
    for i in range(0,a):
# This "-" part of code has same logic as explained before
        if a!=0 and a>=i:
            print("-",end="")
# In this section we are not supposed to print any extra alphabet
# other than the one which is printed in previous section
# Also we do not want to print any "-" to seperate alphabet
# since there is only one alphabet
# therefore when the program is in first line this loop will not get executed
        if a==0:
            break
# Now, if we are not in the first line, then we have to print
# an alphabet which has higher value than the previously printed alphabet
# since we are printing from the centre to right portion
# we need to increase the value of alphabet in each step/iteration
# until we reach the maximum alphabet
# after print function we used continue function to print all the alphabets
# that are necessary in that particlar line then we'll come out of this loop
        else:
            print(list[n-a+i], end="")
            continue
# This print function performs the same operation as the first print function 
# in the loop , but it prints "-" after the printing of alphabets in a particular line
    
    print("-"*(2*n-2*a-2))

# Now , we move on to the lower n-1 lines of the output
# Even this part of the program is divided into two parts
# The first part deals with printing of down-left to down-center portion of rangoli  

# Here the range of 'a' i.e the range of number of lines is upto 'n-1'
# Since number of lines in the lower half are one less than the number of lines
# in the upper half
for a in range(0,n-1):
# If you observe in the print function the number of times the string concatenation
# done was changed. Here we have to start with fewer "-" marks and we have to increase them
# by a step of two
    print("-"*(2*a+2), end="")
# here we have defined range in the for loop in reverse order
# this has two objectives:
# 1) it will be easy to print the alphabets when we start from higher order
#    since we have to start printing the alphabet in higher to lower order
# 2) number of iterations run to print the alphabets has to be reduced each time
#    as 'a' value increases.
    for i in range(n-1,a,-1):
        print(list[i], end="")
# as we've discussed earlier, when we print the left portion we need to print 
# "-" after atleast one alphabet is printed and the line has more than one alphabet to be printed  
# in the left portion of the rangoli 
        if i>a+1:
            print("-",end="")
# This portion of the code deals with bottom right portion of rangoli
# here also were using dynamic range to reduce the number of iterations to reduce 
# the printing of alphabtes in each time
# we have started from range 0 because we need to print the lower level alphabet first
# in each iteration. therefore to accomodate both reduction of range and start
# printing the alphabet from lower level alphabet we've used this range '0' to 'n-2-a'
    for i in range(0,n-2-a):
# This conditional statement breaks the loop as and when the line value 'a' reaches n-2

        if a==n-2:
            break
# until the last line is reached this part prints the the alphabets from lower order first
# in addition to make it is easy we have cncatenated "-" to the next alphabet that has to be printed
# so we did not use any code to print "-" in this part of code
        else:
            print("-"+list[a+i+2],end="")
# this print function performs what the first print function of the bottom half perfoems
# excpet that it prints the "-" after all the alphabets in that line got printed
# and we did not use end="" in the print function in order to facilitate t move to the next 
# line of the output
    print("-"*(2*a+2))
