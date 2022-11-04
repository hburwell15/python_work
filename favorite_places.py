favorite_places = {
	'christian': ['barton springs', 'my lovers house', 'chipotle'], 
	'hannah': ['schlitterbahn' , 'christians bed', 'home'], 
	'andy': ['pool', 'coffee shop', 'navy'],
}

for name, places in favorite_places.items():
	print(f"\n{name.title()}'s favorite places are:")
	for place in places:
		print(f"\t{place.title()}")