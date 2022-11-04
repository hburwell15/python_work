rivers = {
	'nile': {
		'location': 'egypt', 
		'length': '4,142 miles', 
		},

	'amazon': {
		'location': 'south africa',
		'length': '4,345', 
		}, 

	'mississippi': {
		'location': 'america',
		'length': '2,340',  
		},

}

for famous_rivers, cool_info in rivers.items():
	print(f"\nRiver: {famous_rivers.title()}")
	location = f"{cool_info['location']}"
	length = f"{cool_info['length']}"

	print(f"\tLocation: {location.title()}")
	print(f"\tLength: {length.title()}")	