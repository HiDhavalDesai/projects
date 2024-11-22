# This is a quiz game.
# The goal of the game is to get as many questions as you can correctly.

print("Welcome to the Quiz Game!")
print("Let's see how many questions you can answer correctly.")
print("There are a total of 10 questions.")

score = 0

q1 = input("Question 1 - What is the smallest unit of life in biology? ")
if q1.upper() == "CELL":
        score = score +1
        print(f"Correct! Your score is {score}")
else: 
    print("Incorrect Answer. The correct answer is CELL.")


q2 = input("Question 2 - In economics, what term refers to the study of individual consumers and businesses in decision-making? ")
if q2.upper() == "MICROECONOMICS":
        score = score +1
        print(f"Correct! Your score is {score}")
else: 
    print("Incorrect Answer. The correct answer is MICROECONOMICS.")


q3 = input("Question 3 - Who is the author of the 1922 novel Ulysses? ")
if q3.upper() == "JAMES JOYCE":
        score = score +1
        print(f"Correct! Your score is {score}")
else: 
    print("Incorrect Answer. The correct answer is JAMES JOYCE.")


q4 = input("Question 4 - What is the chemical formula for table salt? ")
if q4.upper() == "NACL":
        score = score +1
        print(f"Correct! Your score is {score}")
else: 
    print("Incorrect Answer. The correct answer is NACL.")


q5 = input("Question 5 - What is the term in logic for a statement that is always true regardless of the truth values of its components? ")
if q5.upper() == "TAUTOLOGY":
        score = score+1
        print(f"Correct! Your score is {score}")
else: 
    print("Incorrect Answer. The correct answer is TAUTOLOGY.")


q6 = input("Question 6 - What is the most abundant gas in Earth's atmosphere? ")
if q6.upper() == "NITROGEN":
        score = score+1
        print(f"Correct! Your score is {score}")
else: 
    print("Incorrect Answer. The correct answer is NITROGEN.")


q7 = input("Question 7 - In computer science, what does the acronym CPU stand for? ")
if q7.upper() == "CENTRAL PROCESSING UNIT":
        score = score+1
        print(f"Correct! Your score is {score}")
else: 
    print("Incorrect Answer. The correct answer is CENTRAL PROCESSING UNIT.")


q8 = input("Question 8 - What is the standard SI unit of force? ")
if q8.upper() == "NEWTON":
        score = score+1
        print(f"Correct! Your score is {score}")
else: 
    print("Incorrect Answer. The correct answer is NEWTON.")


q9 = input("Question 9 - In mathematics, what is the value of the golden ratio, rounded to two decimal places? ")
if q9.upper() == "1.62":
        score = score+1
        print(f"Correct! Your score is {score}")
else: 
    print("Incorrect Answer. The correct answer is 1.62.")

q10 = input("Question 10 - In psychology, what is the term for the phenomenon where people perform better on tasks when they are being watched? ")
if q10.upper() == "SOCIAL FACILITATION":
        score = score+1
        print(f"Correct! Your score is {score}")
else: 
    print("Incorrect Answer. The correct answer is SOCIAL FACILITATION.")

print(f"Your final score is {score}")
if score <=5:
        print("You should try again. You can do better!")
elif score > 5 and score <= 8:
        print("Nice effort! You should try again.")
else:
        print("Oh WOW that's a nice score!")

print("Thanks for Playing!")

