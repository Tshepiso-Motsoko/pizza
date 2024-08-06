import sys
import csv
from tabulate import tabulate

def create_pizza_table(filename):
    # Check if the filename ends with .csv
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(filename, newline="") as file:
            # Read the CSV file using DictReader
            reader = csv.DictReader(file)
            data = list(reader)

            # Format the table using tabulate
            table = tabulate(data, headers="keys", tablefmt="grid")

            # Print the table
            print(table)

    except FileNotFoundError:
        sys.exit("File does not exist")


def main():
    # Check the number of command-line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # Get the filename from command-line argument
    filename = sys.argv[1]

    # Create the pizza table
    create_pizza_table(filename)


if __name__ == "__main__":
    main()
