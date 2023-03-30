from caesar_cypher_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

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

    print(f"\nYour {cypher_direction}d text is: {end_text}")

should_restart = True
while should_restart:
    invalid_answer = False
    while not invalid_answer:
        direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        
        if direction != "encode":
            if direction != "decode":
                print("I do not understand this input.\n")
            else:
                invalid_answer = True
        else:
            invalid_answer = True

    text = input("\nType your message:\n").lower()
    shift = int(input("\nType the shift number:\n"))
    shift = shift % 26

    caesar(starting_text = text, shift_amount = shift, cypher_direction = direction)

    user_answer = False
    while not user_answer:
        result = input("\nWould you like to restart the cypher program? Type 'yes' or 'no'\n").lower()

        if result == 'no':
            print("\nGoodbye\n")
            should_restart = False
            break
        elif result != "yes":
            print("I do not understand this input.\n")
            user_answer= False
        else:
            user_answer= True
