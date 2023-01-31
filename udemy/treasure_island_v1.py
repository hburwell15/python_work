game_over = False

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

while game_over == False:
  left_or_right = input('You come to a fork in the road. Do you venture left or right? Type "left" or "right"\n').lower().strip()
 
  if left_or_right == "left":
    while game_over == False:
      swim_or_wait = input('\nYou walk to the shore. It\'s very foggy out on the water. \nDo you swim or wait? Type "swim" or "wait"\n').lower().strip()
      if swim_or_wait == "wait":
        while game_over == False:
          cat = input('\nA small boat drifts out of the fog to the shore. Out jumps a black cat. He looks at you for a long moment. \nDo you pet or ignore? Type "pet" or "ignore"\n').lower().strip()
          if cat == "pet":
            while game_over == False:
              houses = input('\nThe cat accepts your pets and gives you +1 Luck. \nYou take the boat to the island. There are 3 houses in front of you. \nDo you choose red, blue or yellow? Type "red", "blue", or "yellow"\n').lower().strip()
              if houses == "yellow":
                print("You walk into the house to find a large chest sitting in the corner. You open it to see it's full of treasure. \nYOU WIN!")

              elif houses == "blue":
                game_over = True
                print("\nYou see a wizard sitting and having his afternoon tea. He immediatly turns you to ice. He was never one for unwanted visitors. \nGame Over.")

              elif houses == "red":
                game_over = True
                print("\nYou see you've walked into a corporate business meeting. Everyone glares at you and you die from embaressment. \nGame Over.")
              else:
                print("\nI do not recognize this input, please try again")

          elif cat == "ignore":
            while game_over == False:
              houses = input('\nYou ignore the cat and get in the boat. The cat flicks its tail at you dismissivle and walks away into the fog. \nYou arrive at the island where there are 3 house. \nDo you choose red, blue or yellow? Type "red", "blue", or "yellow"\n').lower().strip()
              if houses == "yellow":
                print("\nYou walk into the house to find a large chest sitting in the corner. You open it to see it's full of treasure. \nYOU WIN!")

              elif houses == "blue":
                game_over = True
                print("\nYou see a wizard sitting and having his afternoon tea. He immediatly turns you to ice. He was never one for unwanted visitors. \nGame Over.")
                
              elif houses == "red":
                game_over = True
                print("\nYou see you've walked into a corporate business meeting. Everyone glares at you and you die from embaressment. \nGame Over.")
              else:
                print("\nI do not recognize this input, please try again")

          else:
            print("\nI do not recognize this input, please try again")  
      elif swim_or_wait == "swim":
        game_over = True
        print("You are sequced by sirens and drown.\nGame Over.")
      else:
        print("\nI do not recognize this input, please try again.")
          
  elif left_or_right == "right":
    game_over = True
    print("You have fallen into quicksand. \nGame Over.")
  else:
    print("\nI do not recognize this input, please try again.")
     