# --------------------------------------------
# Python Basics Demonstration Program
# --------------------------------------------


name = "Suvarna"
age = 34
height = 5.4
is_working = True

print("Step 1: Variable Declaration")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Working Status:", is_working)

print("\n----------------------------------")

print("Step 2: Displaying Data Types")
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of is_working:", type(is_working))

print("\n----------------------------------")

print("Step 3: Taking User Input")

student_name = input("Enter your name: ")
student_age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

print("\nYou entered the following details:")
print("Student Name:", student_name)
print("Student Age:", student_age)
print("Marks:", marks)

print("\n----------------------------------")


print("Step 4: Arithmetic Operations")

num1 = 20
num2 = 10

print("First Number:", num1)
print("Second Number:", num2)

print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)
print("Division =", num1 / num2)
print("Modulus =", num1 % num2)

print("\n----------------------------------")

print("Step 5: String Concatenation")

greeting = "Hello"
message = greeting + " " + student_name

print(message)

print("\n----------------------------------")

print("Step 6: Type Conversion")

number_string = "100"

print("Original Value:", number_string)
print("Original Type:", type(number_string))

number = int(number_string)

print("Converted Value:", number)
print("Converted Type:", type(number))

salary = 75000
salary_string = str(salary)

print("Salary as String:", salary_string)
print("Type:", type(salary_string))

decimal_number = float(25)

print("Float Value:", decimal_number)
print("Type:", type(decimal_number))

print("\n----------------------------------")

print("Program Completed Successfully!")
