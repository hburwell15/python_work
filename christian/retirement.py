def calculate_years_to_retirement(current_age, retirement_age):
    '''Calculate how many years until retirement'''
    return retirement_age - current_age

name = input("What is your name? ")
age = int(input("What is your age? "))
RETIREMENT_AGE = 65

print(f"{name} has this many years until retirement: {calculate_years_to_retirement(age, RETIREMENT_AGE)}")