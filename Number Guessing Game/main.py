import random
import time
import sys

class NumberGuessingGame:
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.total_games = 0
        
    def print_with_animation(self, text, delay=0.03):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def display_welcome(self):
        print("=" * 50)
        self.print_with_animation("Welcome to the Ultimate Number Guessing Game!")
        print("=" * 50)
        time.sleep(0.5)
        
        self.print_with_animation("I'm thinking of a number... Can you guess it?")
        self.print_with_animation("You'll get points based on how quickly you guess correctly.")
        self.print_with_animation("The harder the difficulty, the more points you can earn!")
        print()
    
    def choose_difficulty(self):
        self.print_with_animation("Choose your difficulty level:")
        self.print_with_animation("1. Easy (1-10, 5 attempts)")
        self.print_with_animation("2. Medium (1-50, 7 attempts)")
        self.print_with_animation("3. Hard (1-100, 10 attempts)")
        self.print_with_animation("4. Expert (1-500, 12 attempts)")
        
        while True:
            try:
                choice = int(input("\nEnter your choice (1-4): "))
                if 1 <= choice <= 4:
                    return choice
                else:
                    self.print_with_animation("Please enter a number between 1 and 4.")
            except ValueError:
                self.print_with_animation("That's not a valid number. Please try again.")
    
    def setup_game(self, difficulty):
        if difficulty == 1:
            range_min, range_max = 1, 10
            max_attempts = 5
            points_multiplier = 1
        elif difficulty == 2:
            range_min, range_max = 1, 50
            max_attempts = 7
            points_multiplier = 2
        elif difficulty == 3:
            range_min, range_max = 1, 100
            max_attempts = 10
            points_multiplier = 3
        else:  # Expert
            range_min, range_max = 1, 500
            max_attempts = 12
            points_multiplier = 5
        
        secret_number = random.randint(range_min, range_max)
        return secret_number, range_min, range_max, max_attempts, points_multiplier
    
    def get_hint(self, guess, secret_number, attempts, max_attempts):
        difference = abs(guess - secret_number)
        range_size = (secret_number - guess) > 0  
        
        if attempts == max_attempts - 1:  # Last attempt
            return "This is your last chance! The number is {}.".format(
                "even" if secret_number % 2 == 0 else "odd")
        
        if difference == 0:
            return "You got it!"
        elif difference <= 5:
            return "Very close! The number is {}.".format("higher" if range_size else "lower")
        elif difference <= 15:
            return "Close! The number is {}.".format("higher" if range_size else "lower")
        elif difference <= 30:
            return "Not too far. Try {}.".format("higher" if range_size else "lower")
        else:
            return "Way off! The number is much {}.".format("higher" if range_size else "lower")
    
    def play_round(self):
        difficulty = self.choose_difficulty()
        secret_number, range_min, range_max, max_attempts, points_multiplier = self.setup_game(difficulty)
        
        print("\n" + "="*50)
        self.print_with_animation(f"I'm thinking of a number between {range_min} and {range_max}.")
        self.print_with_animation(f"You have {max_attempts} attempts to guess it.")
        print("="*50)
        
        attempts = 0
        start_time = time.time()
        
        while attempts < max_attempts:
            attempts_left = max_attempts - attempts
            self.print_with_animation(f"\nAttempts left: {attempts_left}")
            
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                self.print_with_animation("Please enter a valid number.")
                continue
            
            if guess < range_min or guess > range_max:
                self.print_with_animation(f"Please enter a number between {range_min} and {range_max}.")
                continue
            
            attempts += 1
            
            if guess == secret_number:
                end_time = time.time()
                time_taken = end_time - start_time
                
                # Calculate score based on time and attempts
                base_score = 1000 // attempts
                time_bonus = max(0, 500 - int(time_taken * 10))
                total_round_score = (base_score + time_bonus) * points_multiplier
                self.score += total_round_score
                
                print("\n" + "🎉" * 20)
                self.print_with_animation(f"Congratulations! You guessed the number in {attempts} attempts!")
                self.print_with_animation(f"Time taken: {time_taken:.2f} seconds")
                self.print_with_animation(f"Score for this round: {total_round_score}")
                self.print_with_animation(f"Total score: {self.score}")
                print("🎉" * 20)
                
                if self.score > self.high_score:
                    self.high_score = self.score
                    self.print_with_animation("🏆 NEW HIGH SCORE! 🏆")
                
                break
            else:
                hint = self.get_hint(guess, secret_number, attempts, max_attempts)
                self.print_with_animation(hint)
        else:
            self.print_with_animation(f"\nSorry, you've run out of attempts!")
            self.print_with_animation(f"The number was {secret_number}.")
    
    def play_again(self):
        while True:
            choice = input("\nWould you like to play again? (y/n): ").lower()
            if choice in ['y', 'yes']:
                return True
            elif choice in ['n', 'no']:
                return False
            else:
                self.print_with_animation("Please enter 'y' or 'n'.")
    
    def display_stats(self):
        print("\n" + "="*50)
        self.print_with_animation("GAME STATISTICS")
        print("="*50)
        self.print_with_animation(f"Total games played: {self.total_games}")
        self.print_with_animation(f"Final score: {self.score}")
        self.print_with_animation(f"High score: {self.high_score}")
        print("="*50)
    
    def run(self):
        self.display_welcome()
        
        play = True
        while play:
            self.play_round()
            self.total_games += 1
            play = self.play_again()
        
        self.display_stats()
        self.print_with_animation("\nThanks for playing! Come back soon!")

if __name__ == "__main__":
    game = NumberGuessingGame()
    game.run()