 #################Employee Payroll System#############################
empCount = int(input("Enter no. of employees "))
print(empCount)

highest_salary =0
lowest_salary =0
highest_employee =""
total_payroll = 0

for i in range(empCount) :
    print("\n employee count ",i)

    name = input("\nEnter employee name :")
    salary_per_day = float(input("\nEnter salary per day :"))
    days_present = int(input("\nEnter no of days present :"))
    late_days = int(input("\nEnter no of late days  :"))

    gross_salary = salary_per_day* days_present

    if late_days <= 2:
        deduction_percentage = 0
    elif late_days <= 5:
        deduction_percentage = 5
    elif late_days <=10 :
        deduction_percentage = 10
    elif late_days <= 20 :
        deduction_percentage = 20

    deduction_amount = gross_salary * deduction_percentage /100

    final_salary = gross_salary - deduction_percentage

        # Display Employee Details
    print("\n------ Salary Slip ------")
    print("Employee Name :", name)
    print("Gross Salary  :", gross_salary)
    print("Deduction     :", deduction_amount)
    print("Final Salary  :", final_salary)

    total_payroll = +final_salary

if i==0 or final_salary >highest_salary:
    highest_salary = final_salary
    highest_employee = name

if i==0 or final_salary < lowest_salary :
    lowest_salary = final_salary

    # Company Summary
print("\n========== COMPANY PAYROLL SUMMARY ==========")
print("Highest Salary            :", highest_salary)
print("Lowest Salary             :", lowest_salary)
print("Total Company Payroll     :", total_payroll)
print("Employee Earning Maximum  :", highest_employee)