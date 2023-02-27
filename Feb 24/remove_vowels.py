def remove_vowels_list(characters): # ["a", "e", "b"] 
    index = 0 # initialize index
    while index < len(characters): # run while until end of list
        if characters[index] in "aeiou": # check if item is vowel
            characters.pop(index) # remove item
        else:
            # only increment index if there was no popping
            index += 1 

def remove_vowels_string(string):
    index = 0 # initialize index
    new_string = "" # create result var
    while index < len(string):
        if string[index] not in "aeiou": # check if consonant
            new_string += string[index] # concatenate if consonant
        index += 1 # move on the next character
    return new_string # return results

def indices_of_vowels(string):
    index = 0 # initialize index
    new_list = [] # create result list
    while index < len(string):
        if string[index] in "aeiou": # check if it's a vowel
            new_list.append(index) # append to result if vowel
        index += 1
    return new_list # return results

def main():
    test_list = ["a", "e", "b"] 
    remove_vowels_list(test_list)
    print(test_list) # ["b"]

    print( remove_vowels_string("banana") ) # bnn

    print( indices_of_vowels("aei")) # [0, 1, 2]
    print( indices_of_vowels("") ) # []

main()