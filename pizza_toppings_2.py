message = "Please tell me what toppings you would like: "
message += "\nEnter 'quit' when you are done."
toppings = " "
while toppings != 'quit':
    toppings = input(message)
    if toppings != 'quit':
        print(f"I will add {toppings} to your pizza!")
