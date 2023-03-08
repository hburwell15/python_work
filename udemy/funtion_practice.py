# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
  print("Hello, my name is Hannah.")
  print("I like your shoes!")
  print("What's your name?")

greet()

#Function with an input

def greet_with_name(name):
  print(f"How are you {name}?")
  print(f"Isn't this nice weather {name}?")

greet_with_name("George")

#Function with more than one input

def greet_with(name, location):
  print(f"Hello {name}, isn't {location} beautiful?")


greet_with(name = "Bonnie", location = "Portland")