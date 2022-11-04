my_pizzas = ['pepperoni', 'white', 'cheese']
friend_pizzas = my_pizzas[:]
my_pizzas.append('mushroom')
friend_pizzas.append('sausage')
print("My favorite pizzas are:")
for my_pizza in my_pizzas:
	print(my_pizza)
print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
	print(friend_pizza)