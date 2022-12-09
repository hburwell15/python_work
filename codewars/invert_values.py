def invert(lst):
    inverted_list = []
    for check_list in lst:
        if check_list < 0:
            inverted_list.append(abs(check_list))
        if check_list > 0:
            inverted_list.append(-abs(check_list))
        if check_list == 0:
            inverted_list.append(0)
    return inverted_list
print(invert([1475938,-28347,24957,0,-44573,-2435067,0,104849]))

# you could do the drawn out above option, OR, you can use list comprehension to multiply all of the numbers in the list by -1
# so they will all be inverted when passed through the loop

def invert(lst):
    return [n*-1 for n in lst]
print(invert([1475938,-28347,24957,0,-44573,-2435067,0,104849]))

def invert(lst):
    for l in lst:
        return l*-1
print(invert([1475938,-28347,24957,0,-44573,-2435067,0,104849]))