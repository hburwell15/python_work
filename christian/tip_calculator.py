"""
Write a function called tip_calculator that takes a bill amount and outputs a tip amount.

The tip multiplier should be 0.15 (15%) if the bill amount is between $20 and $200.

Otherwise the tip multiplier should be 0.2 (20%).

Call the function with a variety of bill amounts.

NEXT EXERCISE: print out total (bill+tip)
"""
def tip_calculator(bill_amount):
    "Calculate the tip amount for the bill"
    tip = 0
    if bill_amount > 20 and bill_amount < 200:
       tip = bill_amount * 0.15
    else:
       tip = bill_amount * 0.20
    return tip

tip_calculator(30)

bill_amount = 30
tip_amount = tip_calculator(bill_amount)
print(bill_amount + tip_amount)