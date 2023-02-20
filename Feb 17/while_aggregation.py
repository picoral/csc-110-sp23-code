def factorial(number): # 4 --- 1 * 2 * 3 * 4
    current_integer = 1 # init. var
    product = 1
    while current_integer <= number: # var in cond
        product = product * current_integer
        current_integer += 1 # change var

    return product

def power(base, exp): # 2, 3 --- 2 * 2 * 2
    result = 1
    index = 1
    while index <= exp:
        result = result * base
        index += 1

    return result

def main():
    print( power(2, 3) ) # 8
    print( power(10, 0) ) # 1
    print( power(2, 2) ) # 4
 
main()