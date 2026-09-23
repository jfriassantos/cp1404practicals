MINIMUM_LENGTH = 8


def main():
    password = get_password()
    print_stars(password)


def print_stars(password: str):
    for i in range(len(password)):
        print("*", end="")


def get_password() -> str:
    password = input("Enter Password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Password does not meet length requirements!")
        password = input("Enter Password: ")
    return password


main()
