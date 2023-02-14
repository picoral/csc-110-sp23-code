def vowels_only(string):
    new_string = ""
    index = 0 # initialize index
    while index < len(string):
        if string[index] in "aeiou":
            new_string = new_string + string[index]
        index += 1

    return new_string