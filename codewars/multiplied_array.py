def grow(array):
    total = 1
    for multiplied_array in array:
        total *= multiplied_array
    return total

print(grow([1,2,3,4,5]))