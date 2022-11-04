"""
Write a function that takes a `birth_year` and `current_year` as input. (current_year is a relative term and can actually be any year value)

The function should output the age the person born in `birth_year` will be in `current_ year`.

Call the function with a variety of inputs in the code, and print each result.

NEXT EXERCISE: use an f-string for your print statement if you haven't already

FINAL EXERCISE: use a list to hold several birth_years and loop through them to print out the ages
"""

def persons_age(birth_year, current_year):
    """Calculate how old the person will be in a given year"""
    current_age = (current_year - birth_year)
    return current_age
    

birth_years = []
current_years = [2050, 2076, 2200, 2025, 2034]
for c_year in current_years:
    for b_year in birth_years:
        print(f"Someone born in {b_year} will be {persons_age(b_year, c_year)} in {c_year}")