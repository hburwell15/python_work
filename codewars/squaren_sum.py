def square_sum(numbers):
    total = 0
    for number in numbers:
       total += number **2
    return total

print(square_sum([1,2,3,4]))
