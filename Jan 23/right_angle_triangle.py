def sqrt(n):
    '''
    This function calculates the square root of n
    Args:
      n: an integer
    Returns:
      A float representing the square root of n
    '''
    return n**0.5

def hypotenuse(a, b):
    '''
    This function follows the Pythagorean theorem to calculate
    the hypotenuse of a right angle triangle
    Args:
      a, b: integers or floats representing the short sides of
      of a right triangle
    Returns:
      Rounded float representing the hypotenue of a right 
      triangle
    '''
    c = sqrt(a**2 + b**2)
    return round(c, 2)

def main(): 
    print(sqrt(25))

    result = hypotenuse(3, 4)
    print(result)

    result = hypotenuse(10, 10)
    print(result)

main()