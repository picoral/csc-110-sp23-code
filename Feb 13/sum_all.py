def sum_all(low, high): 
    current_integer = low # initialize index
    total = 0

    while current_integer <= high: # use index in condition
        total = total + current_integer
        current_integer += 1 # increment index

    return total

def main():
    print( sum_all(2, 4) ) # 9
    print( sum_all(1, 2) ) # 3
    print( sum_all(0, 5) ) # 15
    # write two more test cases
    print( sum_all(5, 2) ) # 0
    print( sum_all(-2, 2) ) # 0
    print( sum_all(0.4, 2) ) # 1.8
    print( sum_all(0, 2.4) ) # 3


main()