#Code that prints Fizz for every number from 1-100 that is divisable by 3, prints Buzz if the number is divisable by 5, and prints FizzBuzz if it is divisable by both 3 & 5.

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    if number % 3 == 0:
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    else:
        print(number)