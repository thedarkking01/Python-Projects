# replace ___ with your code

# define a list of numbers
lst = [1, 0, 2, 0, 4, 0, 6, 5]

# loop through each number in the list
for i in lst[:]:

    # if the number is 0
    if i==0:

        # remove the number from the list
        lst.remove(i)

        # also add the number to the end of the list
        lst.append(i)

# print the list
print(lst)