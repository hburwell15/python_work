age = input("What is your age? ")
age = int(age)
if age < 3:
    print("Your ticket will be free!")
elif age in range(3,13):
    print("Your ticket will be $10")
else:
    print("Your ticket will be $15")