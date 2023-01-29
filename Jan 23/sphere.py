def sphere_area(radius):
    a = 4 * 3.1415 * radius**2
    a = round(a, 2)
    return a

def sphere_volume(radius):
    v = (4/3) * 3.1415 * radius**3
    # it returns rounded v with two decimals
    return round(v, 2)

def main():
    radius = .75
    result = sphere_area(radius)
    print(result)

    result = sphere_volume(radius)
    print(result)

main()