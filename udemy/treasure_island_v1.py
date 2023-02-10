game_over = False

def prompt(output):
  return input(output).strip().lower()

def which_house(cat_string, game_over):
  while game_over == False:
    houses = prompt(f'\n{cat_string}\nYou take the boat to the island. \nThere are 3 houses in front of you. \n\nDo you choose red, blue or yellow? Type "red", "blue", or "yellow"\n\n>> ')

    if houses == "yellow":
      print("\nYou walk into the house to find a large chest sitting in the corner. You open it to see it's full of treasure.\n\nYOU WIN!\n")
      return True

    elif houses == "blue":
      print("\nYou see a wizard sitting and having his afternoon tea. He immediatly turns you to ice. He was never one for unwanted visitors.\n\nGAME OVER.\n")
      return True

    elif houses == "red":
      print("\nYou see you've walked into a corporate business meeting. Everyone glares at you and you die from embarrassment.\n\nGAME OVER.\n")
      return True

    else:
      print("\nI do not recognize this input, please try again\n")


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
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.\n\n")

while game_over == False:
  left_or_right = prompt('You come to a fork in the road. \nDo you venture left or right? Type "left" or "right"\n\n>> ')

  if left_or_right == "left":
    while game_over == False:
      swim_or_wait = prompt('\nYou walk until you reach the shore of a large lake.\nIt\'s very foggy out on the water, and you can barley make out the trees and some kind of building on an island in the middle of the lake. \n\nDo you swim or wait? Type "swim" or "wait"\n\n>> ')

      if swim_or_wait == "wait":
        while game_over == False:
          cat = prompt('\nA small boat drifts out of the fog to the shore. Out jumps a black cat. \nHe looks at you for a long moment. \n\nDo you pet or ignore? Type "pet" or "ignore"\n\n>> ')

          if cat == "pet":
            game_over = which_house('The cat accepts your pets and gives you +1 Luck.', game_over)

          elif cat == "ignore":
            game_over = which_house('\nYou ignore the cat and get in the boat. The cat flicks its tail at you dismissively and walks away into the fog.', game_over)

          else:
            print("\nI do not recognize this input, please try again\n")

      elif swim_or_wait == "swim":
        game_over = True
        print("\nYou wade into the chilly water. Luckily you know how to swim.\n\nYou begin to hear a soothing melody and angelic voice singing from below the water's surface.\nYou dive down to investigate and can see nothing but the inky depths, but the voice and melody have gotten louder.\nYou swim further down and feel your chest start to burn, but you need to know what is making that beautiful sound.\nAs you vision starts to fade you see it.\n\nA mess of tenticles and eyes and mouths that emit the most beautiful music you've ever heard.\n\nYour last breath of air bubbles to the surface as you are swallowed by the lake. \n\nGAME OVER.\n")

      else:
        print("\nI do not recognize this input, please try again.")
          
  elif left_or_right == "right":
    game_over = True
    print("\nYou confidently walk down the right path. The ground is very soft.\n\nToo soft.\n\nYour shoes sink deeper and deeper into the ground. As you struggle to move you sink faster. You realize too late that you have walked right into quicksand.\n\nGAME OVER.\n")

    


  else:
    print("\nI do not recognize this input, please try again.\n")
     