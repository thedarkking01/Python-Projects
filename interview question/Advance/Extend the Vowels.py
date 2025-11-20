# Complete the code below

# define a function
def vowel_repeater(string, n):

    # initialize a variable with all vowels
    vowels = 'aeiou'

    # initialize an empty string
    new_string = ''

    # loop through each character in a string
    for character in string:

        # if the character is in vowels list
        if character.lower() in vowels:

            # add the character n times to the new_string
            new_string += character * n

        # if the character is not in vowels list
        else:

            # add the character as it is to the new_string
            new_string += character

    # return the new_string
    return new_string


# call the function
string = input()
n = int(input())
result = vowel_repeater(string, n)
print(result)