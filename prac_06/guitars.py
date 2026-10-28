from guitar import Guitar


def main():
    """Guitar program that asks user for guitar details and prints a list of guitars."""
    guitars = []
    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: "))
        guitar = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(guitar)
        print(f"{guitar} added")
        print()
        guitar_name = input("Name: ")
    print(f"\n ... snip ... \n")
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} ", end="")
        if guitar.is_vintage():
            print("(vintage)")
        else:
            print()


main()
