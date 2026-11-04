from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    """<>"""
    guitars = load_guitars()
    for guitar in guitars:
        print(guitar)

def load_guitars():
    """Load guitars from file into a list of guitar objects."""
    guitars = []
    in_file = open(FILENAME, 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()
    return guitars

main()
