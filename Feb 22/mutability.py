def make_all_even(numbers):
    index = 0
    while index < len(numbers):
        if numbers[index] % 2 == 1:
            numbers[index] += 1
        index += 1

def main():
    test_list = [1, 2, 3, 4]
    make_all_even(test_list)
    print(test_list)

main()