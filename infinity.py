message = "What city would you like to go to? "
message += "Enter quit when you are done. \n"

city = input(message)
while city != 'quit':
    print(f"I would like to go to {city} too!")