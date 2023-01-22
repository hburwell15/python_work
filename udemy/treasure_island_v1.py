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
print("Your mission is to find the treasure.") 

left_or_right = input("Do you venture Left or Right?\n")
lowercase_left_or_right = left_or_right.lower()

if lowercase_left_or_right == "left":
  swim_or_wait = input("\nYou walk to the shore. It's very foggy out on the water. \nDo you Swim or Wait? ")
  lowercase_swim_or_weight = swim_or_wait.lower()
  if lowercase_swim_or_weight == "wait":
    cat = input("\nA small boat drifts out of the fog to the shore. Out jumps a black cat. He looks at you for a long moment. \nDo you Pet or Ignore? ")
    lowercase_cat = cat.lower()
    if lowercase_cat == "pet":
      houses = input("\nThe cat accepts your pets and gives you +1 Luck. \nYou take the boat to the island. There are 3 houses in front of you. \nDo you choose Red, Blue or Yellow? ")
      lowercase_houses = houses.lower()
      if lowercase_houses == "yellow":
        print("You walk into the house to find a large chest sitting in the corner. You open it to see it's full of treasure. \nYOU WIN!")
      elif lowercase_houses == "blue":
        print("\nYou see a wizard sitting and having his afternoon tea. He immediatly turns you to ice. He was never one for unwanted visitors. \nGame Over.")
      else:
        print("\nYou see you've walked into a corporate business meeting. Everyone glares at you and you die from embaressment. \nGame Over.")
    else:
      houses = input("\nYou ignore the cat and get in the boat. The cat flicks its tail at you dismissivle and walks away into the fog. \nYou arrive at the island where there are 3 house. \nDo you choose Red, Blue or Yellow? ")
      lowercase_houses = houses.lower()
      if lowercase_houses == "yellow":
         print("\nYou walk into the house to find a large chest sitting in the corner. You open it to see it's full of treasure. \nYOU WIN!")
      elif lowercase_houses == "blue":
        print("\nYou see a wizard sitting and having his afternoon tea. He immediatly turns you to ice. He was never one for unwanted visitors. \nGame Over.")
      else:
        print("\nYou see you've walked into a corporate business meeting. Everyone glares at you and you die from embaressment. \nGame Over.")
      
  else:
    print("You attempt to swim across, but are seduced by sirens and drown. \nGame Over.")
  
else:
  print("You have fallen into quicksand. \nGame Over.")