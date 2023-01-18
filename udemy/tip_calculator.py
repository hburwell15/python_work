print("Welcome to the tip calculator")

bill_total = float(input("What was the total of the bill? "))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

num_of_people = int(input("How many people to split the bill? "))

tip_as_percentage = tip / 100

total_tip_amount = bill_total * tip_as_percentage

total_bill = total_tip_amount + bill_total

bill_per_person = total_bill/num_of_people

final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_amount}")