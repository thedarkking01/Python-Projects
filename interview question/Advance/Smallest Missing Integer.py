# define a function that finds the smallest missing number
# in a list to make sequence continuous
def find_smallest_missing(lst):

    # first of all sort the list
    lst.sort()

    # loop through the list using enumerate so that
    # we can get the index and the element
    for i in range(len(lst) - 1):

        # if adding 1 to current element makes the next element,
        # continue the loop as the sequence is continuous
        if lst[i] + 1 == lst[i + 1] or lst[i] == lst[i + 1]:
            continue

        # but if it doesn't,
        # return the value after adding 1 to the current element
        else:
            return lst[i] + 1

    # if all numbers are continuous, return the next number
    return lst[-1] + 1


# call the function
numbers = [2, 4, 6, -1, 5, 1, 0]
missing_number = find_smallest_missing(numbers)
print(missing_number)
