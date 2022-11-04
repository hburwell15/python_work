pets = {
	'artie': {
		'animal': 'dog',
		'owner': 'hannah', 
	}, 

	'cindy': {
		'animal': 'cat', 
		'owner': 'sarah',
	},

	'lucas': {
		'animal': 'snake',
		'owner': 'hannah', 
	},

	'rice': {
		'animal': 'cat', 
		'owner': 'unknown', 
	},

	'sebastian': {
		'animal': 'goat', 
		'owner': 'sherril'
	},

}

for pet_names, info in pets.items():
	print(f"\nPet name: {pet_names.title()}")
	animal_type = f"{info['animal']}"
	owner = f"{info['owner']}"

	print(f"\tAnimal: {animal_type.title()}")
	print(f"\tOwner: {owner.title()}")
