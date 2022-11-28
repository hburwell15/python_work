def fake_bin(x):
    for new_binary in x:
        if new_binary < 5:
            new_binary.replace(new_binary,"0")
        if new_binary >= 5:
            new_binary.replace(new_binary,"1")
    return new_binary

print(fake_bin("123456789"))