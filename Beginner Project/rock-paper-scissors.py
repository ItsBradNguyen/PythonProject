import random

user_wins = 0
computer_wins = 0
moves = ["rock", "paper", "scissors"]


while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit. ").lower()
    if user_input == "q":
        break
    
    if user_input not in moves:
        continue

    random_number = random.randint(0,2)
    # rock = 0, paper = 1, scissors = 2
    computer_output = moves[random_number]
    print(f"Computer plays {computer_output}.")

    if user_input == "rock" and computer_output == "scissors":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_output == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and computer_output == "paper": 
        print("You won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1

        
print(f"You won {user_wins} times.")
print(f"The computer won {computer_wins} times.")
print("Goodbye!")