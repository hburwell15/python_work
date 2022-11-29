def fake_bin(x):
    new_string = ""
    for new_binary in x:
        if int(new_binary) < 5:
            new_string += new_binary.replace(new_binary,"0")
        if int(new_binary) >= 5:
            new_string += new_binary.replace(new_binary,"1")
    return new_string

print(fake_bin("000111199229"))