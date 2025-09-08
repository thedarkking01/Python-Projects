def get_user_input(valid_choices):
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    if user_choice not in valid_choices:
        print("Oops! That's not a valid move. Please try again next time.")
        exit()

    return user_choice