# Introduction
print("Welcome to Quiz!")

# Asks the users if they want to do the quiz
playing = input("Do you want to play? ")

# Recursion
if playing.upper() != "YES":
    quit()

print("Sounds Good! Let's play :)")

# Number of Correct Answers
correct_answers = 0

# Number of Questions
num_of_questions = 0

# Question 1
answer = input("What does CPU stand for? ")
if answer.upper() == "CENTRAL PROCESSING UNIT":
    print("Correct!")
    correct_answers += 1
    num_of_questions += 1
else:
    print("Incorrect!")
    num_of_questions += 1

# Question 2
answer = input("What does GPU stand for? ")
if answer.upper() == "GRAPHICS PROCESSING UNIT":
    print("Correct!")
    correct_answers += 1
    num_of_questions += 1
else:
    print("Incorrect!")
    num_of_questions += 1

# Question 3
answer = input("What does RAM stand for? ")
if answer.upper() == "RANDOM ACCESS MEMORY":
    print("Correct!")
    correct_answers += 1
    num_of_questions += 1
else:
    print("Incorrect!")
    num_of_questions += 1

# Question 4
answer = input("What does PSU stand for? ")
if answer.upper() == "POWER SUPPLY UNIT":
    print("Correct!")
    correct_answers += 1
    num_of_questions += 1
else:
    print("Incorrect!")
    num_of_questions += 1

print(f"You answered {correct_answers} questions correctly out of {num_of_questions} questions!")
print(f"Your score: {correct_answers*100/num_of_questions}%")