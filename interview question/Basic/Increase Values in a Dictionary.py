# replace ___ with your code

# function that increments every player's score by 1
def incrementer(dictionary):

    # for loop that iterates through the dictionary
    # and increments the score by 1
    for i in dictionary:
        dictionary[i]+=1

    # print the updated dictionary
    print(dictionary)


# define the dictionary
player_scores = {
    'Cody': 50,
    'Jack': 57,
    'Seth': 59,
    'Roman': 67,
}

# call the function
incrementer(player_scores)