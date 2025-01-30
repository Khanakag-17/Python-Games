import random

computer_choice = random.choice([-1, 0, 1])
user_choice = input("Enter your choice: ")

user_choice = user_choice.lower()[0]

user_dict = {'s': -1, 'w': 0, 'g': 1}
computer_dict = {-1: 's', 0: 'w', 1: 'g'}

user_num_choice = user_dict[user_choice]

print(f"You chose {user_choice} \nComputer chose {computer_dict[computer_choice]}")

# s loses from g = -1 loses from 1
# w loses from s = 0 loses from -1
# g loses from w = 1 loses from 0

if(computer_choice == -1):
    if(user_num_choice == 0):
        print("You win!")
    elif(user_num_choice == 1):
        print("Computer wins!")
    else:
        print("Same choice")

elif(computer_choice == 0):
    if(user_num_choice == -1):
        print("You win!")
    elif(user_num_choice == 1):
        print("Computer wins!")
    else:
        print("Same choice")

elif(computer_choice == 1):
    if(user_num_choice == 0):
        print("You win!")
    elif(user_num_choice == -1):
        print("Computer wins!")
    else:
        print("Same choice")

else:
    print("Something went wrong")