responses = {}

while True:
    name = input("\nWhat is your name? ")
    response = input("If you could go anywhere in the world, where would you go? ")

    responses[name] = response

    repeat = input("\nWould you like to let another person respond? (yes/ no)")
    if repeat == 'no':
        break


print("\nHere is the list of destinations:")
for name2, response2 in responses.items():
    print(f"{name2} would like to go to {response2}")
print("\n")