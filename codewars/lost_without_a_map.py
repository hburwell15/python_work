def maps(array):
    new_array = []
    for doubled_array in array:
        new_array.append(doubled_array*2)
    return new_array

print(maps([2,3,4,5,6,7]))
