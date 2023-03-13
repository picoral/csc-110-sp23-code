def flatten(numbers):
    new_list = [] # create new list

    # for every index in my outer list
    for i in range(len(numbers)):
        # for every index in my inner list
        for j in range(len(numbers[i])):
            # append individual elements to new_list
            new_list.append(numbers[i][j])

    return new_list # return result

def main():
    print( flatten([]) ) # []
    print( flatten([[1, 2, 3], [4, 5, 6]]) ) # [1, 2, 3, 4, 5, 6]
    print( flatten([[1, 2, 3], [4]]) ) # [1, 2, 3, 4]

main()