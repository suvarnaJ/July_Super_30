# Student Result Management System

students = {}

num = int(input("Enter Number of Students: "))

highest_percentage = 0
lowest_percentage = 0
highest_student = ""
lowest_student = ""
total_percentage = 0
failed_students = 0

for i in range(num):

    print("\nEnter Details of Student", i + 1)

    name = input("Enter Student Name: ").title()

    total = 0

    # Input marks of 5 subjects
    for j in range(1, 6):
        marks = float(input("Enter Marks of Subject " + str(j) + ": "))
        total += marks

    percentage = total / 5

    # Grade Calculation
    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"
        failed_students += 1

    # Store in Dictionary
    students[name] = {
        "Total": total,
        "Percentage": percentage,
        "Grade": grade
    }

    total_percentage += percentage

    # Highest Scorer
    if i == 0 or percentage > highest_percentage:
        highest_percentage = percentage
        highest_student = name

    # Lowest Scorer
    if i == 0 or percentage < lowest_percentage:
        lowest_percentage = percentage
        lowest_student = name

# Average Percentage
average_percentage = total_percentage / num

# Report
print("\n========== STUDENT REPORT ==========")

print("".format("Name", "Total", "Percentage", "Grade"))

for student in students:
    print("".format(
        student,
        students[student]["Total"],
        students[student]["Percentage"],
        students[student]["Grade"]
    ))

print("\n========== CLASS SUMMARY ==========")
print("Highest Scorer        :", highest_student)
print("Highest Percentage    :", highest_percentage)

print("Lowest Scorer         :", lowest_student)
print("Lowest Percentage     :", lowest_percentage)

print("Average Percentage    :", round(average_percentage, 2))
print("Students Failed       :", failed_students)