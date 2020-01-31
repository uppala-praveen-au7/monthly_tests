# 1) Another sorting method, the counting sort, does not require comparison. 
# Instead, you create an integer array whose index range covers the entire range of values in your array to sort. 
# Each time a value occurs in the original array, you increment the counter at that index. 
# At the end, run through your counting array, printing the value of each non-zero valued index that number of times. 
# For example, consider an array . All of the values are in the range , so create an array of zeroes, . 
# The results of each iteration follow:
# i	arr[i]	result
# 0	1	[0, 1, 0, 0]
# 1	1	[0, 2, 0, 0]
# 2	3	[0, 2, 0, 1]
# 3	2	[0, 2, 1, 1]
# 4	1	[0, 3, 1, 1]

# Now we can print the list of occurrences,0 3 1 1  or determine the sorted array: sorted = [1,1,1,2,3]

# Implementation of a counting sort for a list of positive integers
# that too with minimum max value in the list
input_list=[]

len_input_list=int(input('please enter the number of integers you want to give as input: '))
for i in range(len_input_list):
    num=int(input('please enter a positive integer: '))
    input_list.append(num)
print('the input list :', input_list)
rep_list=[0]*(max(input_list)+1)

# Whenever there is an occurence of an element in the original array
# the particular position in the repetition list will be incremented by 1
for i in range(0,len(input_list)):
    for j in range(0,max(input_list)+1):
        if input_list[i]==j:
            rep_list[j]+=1
            continue
        else:
            pass


# The sorted list is obtained by simply multiplying the element that has to be repeated 
# that is [i] with the corresponding elementt in the repetition list and adding them to
# the final_list by using extend method
final_list=[]
for i in range(max(input_list)+1):
    final_list.extend([i]*rep_list[i])
    

print('the sorted list is:',final_list)