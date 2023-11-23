import random as ran

Operation = ran.randint(0, 3)
Question1 = ran.randint(1, 99)
Question2 = ran.randint(1, 99)

if Operation == 0:
    result = Question1 + Question2
    Answer = input(f"What is {Question1} + {Question2}? ")

elif Operation == 1:
    result = Question1 - Question2
    Answer = input(f"What is {Question1} - {Question2}? ")

elif Operation == 2:
    result = round(Question1 / Question2, 2)
    Answer = input(f"What is {Question1} / {Question2}? (Round to nearest hundredths) ")

elif Operation == 3:
    result = Question1 * Question2
    Answer = input(f"What is {Question1} * {Question2}? ")

#Does not take into account runtime errors
if result == eval(Answer):
    print("Correct!")
else:
    print("Incorrect!")
