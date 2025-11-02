# replace ___ with your code

# list of numbers
num_list = [16, 8, 4, 7, 1, 23, 6]
res=[]
# reverse the list using the slicing method
# and store it in reversed_list
for n in range(len(num_list)-1,-1,-1):
    res.append(num_list[n])
# reversed_list = num_list[::-1]

# print the reversed_list
print(res)