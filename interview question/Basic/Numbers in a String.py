# Complete the code below

# define a function
def digits_counter(string):

    # initialize the counter variable
    counter = 0

    # loop through each character in the string
    for character in string:

        # if the character is a digit, increment the counter
        if character.isdigit():
            counter += 1

    # return the counter
    return counter


# call the function
string = input()
result = digits_counter(string)
print(result)