"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""

def main():
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = calculate_celsius_to_farenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit : "))
            celsius = calculate_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def calculate_celsius_to_farenheit(celsius: float) -> float | int:
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def calculate_fahrenheit_to_celsius(fahrenheit: float) -> float | int:
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius

main()
