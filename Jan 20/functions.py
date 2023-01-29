def circle_area(radius):
    area = 3.1415 * radius ** 2
    return round(area, 2)

def cilinder_volume(radius, height):
    area = circle_area(radius)
    volume = area * height
    return volume

def square_area(side):
    area = side * side
    return area

def sphere_volume(radius):
    volume = (4/3) * 3.1415 * radius ** 3
    volume = round(volume, 2)
    return volume

def main():
    result = sphere_volume(2)
    print(result)

    result = square_area(5)
    print(result)

    result = cilinder_volume(3, 4)
    print(result)

    result = circle_area(5)
    print(result)

    result = circle_area(12)
    print(result)

main()

