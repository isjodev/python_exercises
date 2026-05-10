import random

def get_random_number():
    num = random.randint(1,100)
    return num

def guessing_game():
    rand_num = get_random_number()

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
