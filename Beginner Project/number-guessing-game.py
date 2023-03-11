import random

# The Upper Limit of the Number Generation
upper_limit = input("Type a number: ")

# Conditional test if entered value is a positive number
if upper_limit.isdigit():
    upper_limit = int(upper_limit)
    if upper_limit < 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

# Range
rand_num = random.randint(0, upper_limit)

# Num of Guesses
num_of_guesses = 0
# While Loop
while True:
    num_of_guesses += 1
    user_guess = input("Guess the number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        break
    if user_guess < rand_num:
        print("Guess higher!")
    elif user_guess > rand_num:
        print("Guess lower")
    else:
        print("You got it correct!")
        break
    continue

print(f"You guessed {num_of_guesses} times!")