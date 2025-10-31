# replace ___ with your code

# define a function that calculates the amount after discount
def discounter(total, discount):

    # from the total amount and discount percentage,
    # calculate the amount after discount
    actual_discount = (total * discount) / 100

    # calculate the amount after discount
    final_amount = total - actual_discount 

    # print the final amount
    print(final_amount)


# call the function
discounter(100, 10)