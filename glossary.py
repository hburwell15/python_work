glossary = {
	'Boolean expression': 'conditional test',
	'Tuple': 'immutable list',
	'List comprehension': 'allows you to generate the same list in one line of code', 
	'Looping': 'allows you to take the same action with each value in a list', 
	'Index error': 'Python cannot find the item at the index requested', 
	'Rstrip': 'Gets rid of all white space after the last letter', 
	'Title()': 'Capitalizes every first letter of every word in a str', 
	'Strip': 'Gets rid of white space before and after a str', 
	'Floats': 'Any number with a decimal point', 
	'Constants': 'A variable whose value stays the same throughout the life of the program', 
	}
for name, definition in glossary.items():
	print(f"{name.title()}: {definition}\n")
