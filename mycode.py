import os
import csv

os.makedirs("data", exist_ok=True)

file_path = "data/data.csv"

with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["id", "name", "score"])
    writer.writerow([1, "Alice", 90])
    writer.writerow([2, "Bob", 85])

print("CSV file created successfully!")