
import csv
import random

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Student_ID", "Name", "Age",
        "Gender", "Maths", "Science", "English"
    ])

    for i in range(1, 20001):
        writer.writerow([
            i,
            f"Student_{i}",
            random.randint(18, 23),
            random.choice(["Male", "Female"]),
            random.randint(30, 100),
            random.randint(30, 100),
            random.randint(30, 100)
        ])

print("20,000 student records created successfully!")
