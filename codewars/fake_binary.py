def fake_bin(old_string):
    new_string = ""
    for digit in old_string:
        if int(digit) < 5:
            new_string += "0"
        if int(digit) >= 5:
            new_string += "1"
    return new_string

print(fake_bin("000111199229"))