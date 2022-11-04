cities = { 
	'boston': {
		'country': 'america', 
		'population': '689,000', 
		'fact': 'the first Dunkin Donuts was located near Boston', 
	},

	'austin': {
		'country': 'america', 
		'population': '965,000', 
		'fact': 'worlds music capital', 
	}, 

	'hong kong': {
		'country': 'china', 
		'population': '7 million', 
		'fact': 'there are 263 islands in the city',
	},

}

for location_name, location_info in cities.items():
	print(f"\nCity name: {location_name.title()}")
	country = location_info['country']
	population = location_info['population']
	fact = location_info['fact']

	print(f"\tCountry: {country.title()}")
	print(f"\tPopulation: {population.title()}")
	print(f"\tFact: {fact}")
