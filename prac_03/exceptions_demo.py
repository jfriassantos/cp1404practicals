"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
- A ValueError code will occur when the user puts in alphabetical letters or decimal numbers instead of integers.
2. When will a ZeroDivisionError occur?
- A ZeroDivisionError will occur when the user enters 0 as the denominator as you cannot divide by 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
- I could add a valid input check for the denominator that prevents the user from entering 0.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be 0!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")