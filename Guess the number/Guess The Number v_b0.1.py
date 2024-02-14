import random
import time
import os
import turtle as trtl
turtle=trtl.Turtle()
def guessing_game():
    print("Win32_APP running in CMD.exe")
    print("I have selected a random number between 1 and 100. Try to guess it!")

    # Create directory if it doesn't exist
    save_directory = 'C:\\attempts'
    os.makedirs(save_directory, exist_ok=True)

    while True:
        # Generate a random number between 1 and 100 for each new game
        secret_number = random.randint(1, 100)

        attempts = 0

        while True:
            try:
                # Get player's guess
                guess = int(input("Enter your guess: "))

                # Increase the number of attempts
                attempts += 1

                # Check if the guess is correct
                if guess == secret_number:
                    print(f"Congratulations! You guessed the number in {attempts} attempts.")
                    for i in range(attempts):
                        
                        turtle.circle(attempts)
                        
                    # Save attempts to a file
                    save_path = os.path.join(save_directory, f'attempts_{time.time()}.txt')
                    with open(save_path, 'w') as file:
                        file.write(f"Number: {secret_number}\nAttempts: {attempts}")
                    break
                elif guess < secret_number:
                    print("Too low! Try again.")
                else:
                    print("Too high! Try again.")
            except ValueError:
                print("Oof... Only numbers! Sorry!!")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Thanks for playing! Goodbye! Game will close on its own :) Just rerun the .py file to play again!!")
            time.sleep(5)  # 3-second delay
            break

if __name__ == "__main__":
    guessing_game()
