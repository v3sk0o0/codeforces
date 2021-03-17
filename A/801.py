#!/usr/local/bin/python3

keyboard_input = input()


minimal = str(keyboard_input).count("VK")


# ultra brute force
for index, char in enumerate(keyboard_input):

    current = keyboard_input[:index]

    if char == "V":
        current += "K"
    else:
        current += "V"

    current += keyboard_input[index + 1:]

    minimal = max(minimal, current.count("VK"))


print(minimal)
