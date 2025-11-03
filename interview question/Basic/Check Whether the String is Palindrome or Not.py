# replace ___ with your code

# function to check palindrome string
def is_palindrome(text):
    rev_text = ''
    # reverse the string using slicing and
    # store it in the rev_text variable
    for i in range(len(text)-1,-1,-1):
        rev_text+=text[i]

    # compare the reversed string with the original string
    if rev_text==text:
        print('String is Palindrome')
    else:
        print('String is not Palindrome')


# call the function with the string parameter
text = 'hannah'
is_palindrome(text)