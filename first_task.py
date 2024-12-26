def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def find_largest_number(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest


def print_even_numbers():
    for number in range(1, 21):
        if number % 2 == 0:
            print(number, end=" ")
    print()
