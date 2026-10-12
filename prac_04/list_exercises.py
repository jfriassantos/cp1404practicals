def main():
    """Program to get numbers from user and display statistics."""
    numbers = get_numbers("Number: ")
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


def get_numbers(prompt):
    """Return 5 numbers from the user as a list."""
    numbers = []
    for i in range(5):
        number = int(input(prompt))
        numbers.append(number)
    return numbers


main()
