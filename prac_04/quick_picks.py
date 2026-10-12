MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45


def main():
    """Program to create lines of 6 random numbers according to user input."""
    number_of_quick_picks = get_valid_number("How many quick picks? ")
    print_quick_picks(number_of_quick_picks)


def get_valid_number(prompt):
    """Get valid number from user."""
    number = int(input(prompt))
    while number < 0:
        print("Invalid")
        number = int(input(prompt))
    return number


def print_quick_picks(number_of_quick_picks):
    """"""


main()
