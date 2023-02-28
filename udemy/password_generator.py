import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\nWelcome to the PyPassword Generator!\n")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy level: simply prints ou the letters, symbols, and numbers in order 

password = ""

for letter in range(0, nr_letters):
  password += random.choice(letters)

for symbol in range(0, nr_symbols):
  password += random.choice(symbols)

for number in range(0, nr_numbers):
  password += random.choice(numbers)

print(f"Here is your password: {password}")


#Hard level (password is randomized):

password = ""

for letter in range(0, nr_letters):
  password += random.choice(letters)

for symbol in range(0, nr_symbols):
  password += random.choice(symbols)

for number in range(0, nr_numbers):
  password += random.choice(numbers)

final_password = list(password)
random.shuffle(final_password)
print(f"Here is your password: {''.join(final_password)}")

# or for a simplier version that is easier to read:

password_list = []

for letter in range(0, nr_letters):
  password_list += random.choice(letters)

for symbol in range(0, nr_symbols):
  password_list += random.choice(symbols)

for number in range(0, nr_numbers):
  password_list += random.choice(numbers)

random.shuffle(password_list)

new_password = ""
for char in password_list:
    new_password += char

print(f"Here is your password: {new_password}")

