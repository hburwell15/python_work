import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

random_number = random.randint(0, len(names) - 1)
random_name = names[random_number]
print(f"{random_name} will be paying for the meal today")

#Alternate code:

# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")

# random_name = random.choice(names)
# print(f"{random_name} will pay for th meal.")
