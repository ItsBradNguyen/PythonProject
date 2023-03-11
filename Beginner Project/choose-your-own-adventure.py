name = input("Type your name: ").capitalize()
print(f"Welcome {name} to this adventure!")

answer = input("You are on a dirt road, it has come to an end, and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river. You can walk around it or swim across? Type walk to walk around and swim to swim across: ").lower()
    if answer == "walk":
        print("You walked for many miles, ran out of water, and died. You lost the game!")
    elif answer == "swim":
        print("You swam across and were eaten by an alligator.")
    else:
        print("Not a valid option. You lose!")

elif answer == "right":
    answer = input("You come to a bridge, and it looks wobbly. Do you want to cross it or head back (cross/back)? ").lower()
    if answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them? (yes/no)").lower()
        if answer == "yes":
            print("You talk to the stranger, and the stranger gives you money!")
        elif answer == "no":
            print("You ignore the stranger, and the stranger is offended. The stranger attacks you, and you died.")
        else:
            print("Not a valid option. You lose!")
    elif answer == "back":
        print("You got back to the main road safely.")
    else:
        print("Not a valid option. You lose!")
else:
    print("Not a valid option. You lose!")

print(f"Thank you for playing, {name}")