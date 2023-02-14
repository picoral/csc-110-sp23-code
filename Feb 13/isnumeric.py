def is_numeric_one_char(string):
    if len(string) > 1: # check if string is invalid
        return False
    
    # if string is valid
    if string in "0123456789": # check if char is digit
        return True
    else:
        return False
    
def is_numeric(string):
    '''
    '''
    decimal_count = 0
    index = 0 # initialize index
    while index < len(string): # use index in condition
        if string[index] not in "0123456789.":
            return False
        
        if string[index] == ".": # count decimal points
            decimal_count += 1
        
        index += 1 # increment index

    if decimal_count > 1:
        return False
    else:
        return True

    
def main():
    print( is_numeric("5") ) # True
    print( is_numeric("a") ) # False
    print( is_numeric("12") ) # True
    print( is_numeric("1z") ) # False
    print( is_numeric("12.5") ) # True
    print( is_numeric("12.5.5") ) # False

main()