def every_two_together(characters):
    new_string = "" # create new string
    # for every two indiced in my list
    for i in range(0, len(characters), 2):
        # add that character to my new_string
        new_string += characters[i]
    return new_string # return results

def main():
    characters = ["a", "e", "p", "o", "p", "w", "l", "i", "e", "f"]
    print( every_two_together(characters) ) # apple

main()