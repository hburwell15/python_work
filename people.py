people = {
	'sarah': {
		'first': 'sarah',
		'last': 'ferre',
		'age': '29',  
		'city': 'pearland', 
	},

	'katie': {
		'first': 'katie', 
		'last': 'burwell', 
		'age': '31',
		'city': 'league city', 
	},

	'trish': {
		'first': 'trish', 
		'last': 'black', 
		'age': '45', 
		'city': 'league city', 
	}
}
for sisters, personal_info in people.items():
	print(f"\nName: {sisters.title()}")
	full_name = f"{personal_info['first']} {personal_info['last']}"
	age = f"{personal_info['age']}"
	city = f"{personal_info['city']}"

	print(f"\tFull name: {full_name.title()}")
	print(f"\tAge: {age.title()}")
	print(f"\tCity: {city.title()}")