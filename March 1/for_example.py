index = 0
while index < 5:
    print(index)
    index += 1

for index in range(5):
    print(index)

def indices_of_vowels(string):
    result = [] # create empty list
    # for every index in my string
    for index in range(len(string)):
        # check if char at index is a vowel
        if string[index] in "aeiouAEIOU":
            # if vowel, append index of char to result
            result.append(index)
    return result