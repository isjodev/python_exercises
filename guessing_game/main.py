import random

def guessing_game():
    rand_num = randon.randint(1, 100)

    while True:
        user_guess = int(input("Enter guess: "))

        if user_guess == rand_num:
            print(f"Correct!")
            break

        if user_guess < rand_num:
            print(f"Your guess of {user_guess} is too low!")

        else:
            print(f"Your guess of {user_guess} is too high!")


guessing_game()
