import os
import csv

os.makedirs("data", exist_ok=True)

file_path = "data/data.csv"
with open(file_path, "a", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([3, "Charlie", 95])

print("New row added successfully!")
print("CSV file created successfully!")