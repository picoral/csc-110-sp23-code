def max_list(numbers):
    if len(numbers) > 0:
        max = numbers[0]
        index = 0
        while index < len(numbers):
            if numbers[index] > max:
                max = numbers[index]
            index += 1
        return max

def min_list(numbers):
    if len(numbers) > 0:
        min = numbers[0]
        index = 0
        while index < len(numbers):
            if numbers[index] < min:
                min = numbers[index]
            index += 1
        return min

def main():
    print( max_list([1, 2, 3, 1, 2]) ) # 3
    print( max_list([]) ) # None
    print( max_list([1])) # 1

    print( min_list([]) ) # None
    print( min_list([1])) # 1
    print( min_list([1, 2, 3, 0, 2]) ) # 0

main()