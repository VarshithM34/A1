Employee_ID = input("Enter the Employee ID: ")
Employee_Name = input("Enter the Employee Name: ")
Salary = float(input("Enter the Salary: "))

if Salary <= 30000:
    bonus = 0.10
elif Salary <= 50000:
    bonus = Salary * 0.15
else:
    bonus = Salary * 0.20

final_salary = Salary + bonus
print("Employee ID:", Employee_ID)
print("Employee Name:", Employee_Name)
print("Salary:", Salary)
print("Bonus:", bonus)
print("Final Salary:", final_salary)
