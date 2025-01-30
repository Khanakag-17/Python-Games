import random

#Computer chooses a random number between 0 & 100 (Both included)
computer_choice = random.randint(0, 101)

#Starts with atleast 1 guess
guesses = 1

#a = -1 chosen so that the loop keeps going till broken internally
a = -1
while(a < 0):
    user_choice = int(input("Enter a number: "))

    #Checking whether the user choice is valid or not
    if(user_choice > 100 or user_choice < 0):
        print("Invalid choice. Choose a number from 0 to 100.")

    #Comparing with computer's choice
    if(user_choice > computer_choice):
        print("Choose a number lower than the chosen")
        guesses += 1

    elif(user_choice < computer_choice):
        print("Choose a number higher than the chosen")
        guesses += 1

    else:
        print(f"""Correct choice!
You took {guesses} guesses.""")
        break