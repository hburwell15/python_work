#finding the largest number in a list

# numbers = [10, 482, 5729, 10, 383495, 273, 503, 3917, 3840, 485702]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)

# print the words for numbers

phone = input("Phone: ")
translation = ""
numbers_to_words = {"0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    }
for ch in phone:
    translation += numbers_to_words.get(ch) + " "

print(translation)