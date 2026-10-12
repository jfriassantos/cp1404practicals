"""
CP1404/CP5632 Practical
Data file -> lists program
"""
from typing import Any

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    data = load_data(FILENAME)
    print_records(data)


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_records = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        data = [parts[0], parts[1], int(parts[2])]
        subject_records.append(data)
    input_file.close()
    return subject_records


def print_records(records):
    """Print records based on structure with dynamic length for lecturer name."""
    width = max(len(pair[1]) for pair in records)
    for record in records:
        print(f"{record[0]} is taught by {record[1]:{width}} and has {record[2]:3} students")

main()
