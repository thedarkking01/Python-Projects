# replace ___ with your code

# define a list
numbers = [51, 51, 23, 6, 5, 2]

# remove duplicate elements from the list
# by converting it to a set
number_set = set(numbers)

# convert the set back to a list
numbers = list(number_set)

# remove max element of the list
max_number = max(numbers)
numbers.remove(max_number)

# access the new maximum element of the list
# which is the second largest element of the original list
largest_number = numbers[-1]

print(largest_number)