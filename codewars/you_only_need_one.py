def check(seq, elem):
    if elem in seq:
        return True
    else:
        return False

print(check([7,2,2,"hello", 39, "hi", "chair", 2374, "table", 37, "money"], "love"))