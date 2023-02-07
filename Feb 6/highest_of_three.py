def average_of_highest(x, y, z):
    min = x
    if y < min:
        min = y
    if z < min:
        min = z

    return (x+y+z-min)/2

def average_of_highest_1(x, y, z):
    if x >= z  and y >= z: 
        return (x + y) / 2
    elif y >= x and z >= x: 
        return (y + z) / 2
    else:
        return (x + z) / 2

def main():
    print( average_of_highest(1, 3, 5) ) # should print 4.0
    print( average_of_highest(6, 4, 2) ) # should print 5.0
    print( average_of_highest(4, 2, 1) ) # should print 3.0
    print( average_of_highest(2, 2, 1) ) # should print 2.0
    print( average_of_highest(2, 1, 2) ) # should print 2.0
    print( average_of_highest(3, 3, 3) ) # should print 3.0
    print( average_of_highest(3, 1, 1) ) # should print 2.0

main()