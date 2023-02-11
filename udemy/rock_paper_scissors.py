import random 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_image = [rock, paper, scissors]


print("Let's play Rock, Paper, Scissors!")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!")
else:
    print(game_image[user_choice])


    computer_choice = random.randint(0,2)
    print("\nComputer chose: ")
    print(game_image[computer_choice])

    #Condensed alternate code: 
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")

# My original code:

# if user_choice == 0:
#   if computer_choice == 0:
#     print("\nYou tied!")
    
#   elif computer_choice == 1:
#     print("\nYou lose!")
    
#   else:
#     print("\nYou win!")

# if user_choice == 1:
#   if computer_choice == 0:
#     print("\nYou lose!")
    
#   elif computer_choice == 1:
#     print("\nYou tied!")
    
#   else:
#     print("\nYou win!")

# if user_choice == 2:
#   if computer_choice == 0:
#     print("\nYou lose!")
    
#   elif computer_choice == 1:
#     print("\nYou win!")

#   else:
#     print("\You tied!")