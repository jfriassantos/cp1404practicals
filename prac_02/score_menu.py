"""
print menu
get choice
while choice != <quit option>
    if choice == <first option>
        <do first task>
    else if choice == <second option>
        <do second task>
    ...
    else if choice == <n-th option>
        <do n-th task>
    else
        print invalid input error message
    print menu
    get choice
<do final thing, if needed>
"""


def main():
    score = get_valid_score("Enter Score: ", 0, 100)
    print("(G)et A Valid Score \n(P)rint Result \n(S)how Stars \n(Q)uit")
    choice = input("Enter Choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score("Enter Score: ", 0, 100)
        if choice == "P":
            result = determine_score(score)
            print(f"User score {score} is {result}")
        if choice == "S":
            print_stars(int(score))
        print("(G)et A Valid Score \n(P)rint Result \n(S)how Stars \n(Q)uit")
        choice = input("Enter Choice: ").upper()
    print("Farewell Human!")


def get_valid_score(prompt, low, high):
    """Gets valid score with prompt."""
    score = float(input(prompt))
    while score < low or score > high:
        print("Invalid Score.")
        score = float(input(prompt))
    return score


def determine_score(score: float) -> str:
    """Determines result based on score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(amount):
    """Prints amount of stars inputted by user."""
    for i in range(amount):
        print("*", end="")
    print()


main()
