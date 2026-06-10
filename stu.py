Student_Name = input("Enter the Student Name: ")
Marks_Python = float(input("Enter the Marks in Python: "))
Marks_SQL = float(input("Enter the Marks in SQL: "))
marks_excel= float(input("Enter the Marks in Excel: "))

total = Marks_Python + Marks_SQL + marks_excel
avg = total / 3
percentage = (total / 300) * 100

if percentage >= 90:
    grade = "A"
elif percentage >=75 and percentage <=89:
    grade = "B"
elif percentage <=60 and percentage >=74:
    grade = "C"
else:
    print("Fail")
print("Student Name:", Student_Name)
print("Marks in Python:", Marks_Python)     
print("Marks in SQL:", Marks_SQL)
print("Marks in Excel:", marks_excel)   
print("Total Marks:", total)
print("Average Marks:", avg)
print("Percentage:", percentage)
print("Grade:", grade)

    