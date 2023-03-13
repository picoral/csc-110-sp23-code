def detect_duplicate(list_a, list_b): # [2, 1] [1]
    # for every index in list_a
    for index in range(len(list_a)):
        # check if element at index is in list_b
        if list_a[index] in list_b:
            # if so, found a duplicate!
            return True
    # if loop ran without returning True
    return False

def every_two_together(characters):
    new_string = ""
    for i in range(0, len(characters), 2):
        new_string += characters[i]
    return new_string


def main():
    print( detect_duplicate([], []) ) # False
    print( detect_duplicate(["a", "b"], ["c", "d", "a"]) ) # True
    print( detect_duplicate([0, 3, 2, 1, 2, 4], [5, 6, 0]) ) # True

main()