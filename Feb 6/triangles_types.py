def triangle_inequality(x, y, z):
    if x >= y + z or y >= z + x or z >= x + y:
        return False
    else:
        return True

def triangle_type(x, y, z):
    if triangle_inequality(x, y, z):
        if x == y and y == z: # if True then x == z
            return "Equilateral"
        elif x == y or y == z or z == x:
            return "Isosceles"
        else:
            return "Obtuse"
    else:
        return "This is not a real triangle"

def main():
    print( triangle_type(3, 3, 3) ) # "Equilateral"
    print( triangle_type(3, 2, 3) ) # "Isosceles"
    print( triangle_type(4, 5, 6) ) # "Obtuse"
    print( triangle_type(1, 2, 3) ) # "The triangle does not exist"

main()