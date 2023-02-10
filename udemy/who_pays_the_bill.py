import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

random_number = random.randint(0, len(names)-1)
random_name = names[random_number]
print(random_name)