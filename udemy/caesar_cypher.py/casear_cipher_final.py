from caesar_cypher_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

#TODO - make it so if the person types in something other than encode od decode, they get looped back to the prompt
def caesar(starting_text, shift_amount, cypher_direction):
    end_text = ""
    if cypher_direction == "decode":
        shift_amount *= -1

    for char in starting_text:
        if char not in alphabet:
            end_text += char
        else:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]

    print(f"Your {cypher_direction}d text is {end_text}")

should_restart = True
invalid_answer = True
while should_restart:
    while invalid_answer:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#TODO - line 29 is always generating False. Fix this
        if direction != "encode" or direction != "decode":
            print("I do not understand this input. Please type encode or decode.\n")
            invalid_answer = False
            continue
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(starting_text = text, shift_amount = shift, cypher_direction = direction)
    while invalid_answer:
        result = input("Would you like to restart the cypher program? Type 'yes' or 'no'").lower()
        if result != "yes" or result != "no":
            print("I do not understand this input. Please type yes or no.\n")
            invalid_answer = False
            continue
        if result == 'no':
            print("Goodbye")
            should_restart = False