def sum_all(numbers):
    '''
    Args:
      numbers is list
    '''
    index = 0 # initialize index
    total = 0
    while index < len(numbers): # use index in cond
        total += numbers[index]
        index += 1 # increment index

    return total

def max3(x, y, z):
    max = x # assume first number is highest

    if y > max:
        max = y # assume second number is highest

    if z > max:
        max = z # third number is highest

    return max

def max_list(numbers):
    index = 1 # initialize index
    max = numbers[0] # assume max is first item in list
    while index < len(numbers): # use index in cond
        if numbers[index] > max:
            max = numbers[index]
        index += 1 # increment index
    return max

def main():
    print( max_list([1, 2, 1, 5, 2, 1]) ) # 5
    print( max_list([-1, -2, -1, -5, -2, -1]) ) # -1

main()