# bill_amount = 50
# if bill_amount > 20 or bill_amount < 200:
#     print(bill_amount * 0.1

# new_li = ['h', 'e', 'l', 'l', 'o', ' ', 'e', 'v', 'e', 'r', 'y', 'o', 'n', 'e']
# new_str = str(new_li)
# new_li.reverse()
# print(new_li)

# def positive_sum(arr):
#     '''Return the sum of all positive numbers'''
#     positive_numbers = 0
#     for x in arr:
#         if x > 0:
#             positive_numbers = positive_numbers + x
#     return positive_numbers

# positive_sum([1, -2, 6, -10 , 0, 12, -30])

def make_negative( number ):
    if number > 0:
        return number * -1
    return number
    
    

make_negative(42)