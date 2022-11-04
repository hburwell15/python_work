from distutils.util import strtobool

class Pizza:
    def __init__(self, style, toppings):
        self.style = style
        self.toppings = toppings

    def __str__(self):
        return f"{self.style} pizza with {' and '.join(self.toppings)}"

def main():
    while True:
        style = input("What style of pizza do you like, regular or deep-dish? ")
        style = style.lower()
        toppings = input("What toppings do you like? Enter them separated by commas: ")
        toppings = toppings.split(",")

        your_pizza = Pizza(style, toppings)
        print(f"You ordered:\n\t{your_pizza}")

        order_accepted = input("Is this correct? ")
        order_accepted = strtobool(order_accepted)
        if order_accepted:
            print("Great, we'll have your order ready soon!\n\n")
            break
        else:
            print("OK, let's start over and try again.\n\n")

if __name__ == "__main__":
    main()