import csv

def analyze_sales(file_name):
    with open(file_name, "r") as file:
        reader = csv.DictReader(file)

        sales = []

        for row in reader:
            sales.append(float(row["Sales"]))

        average = sum(sales) / len(sales)
        highest = max(sales)
        lowest = min(sales)

        print("Average sales:", average)
        print("Highest sale:", highest)
        print("Lowest sale:", lowest)

analyze_sales("sales.csv")