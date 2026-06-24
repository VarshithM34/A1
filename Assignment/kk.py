stu_1 = int(input("enetr the marks:"))
stu_2 = int(input("enetr the marks:"))
stu_3 = int(input("enetr the marks:"))
stu_4 = int(input("enetr the marks:"))
stu_5 = int(input("enetr the marks:"))

stu_marks = [stu_1, stu_2, stu_3, stu_4, stu_5]
print(stu_marks)

tol_marks =stu_1 + stu_2 + stu_3 + stu_4 + stu_5
print(f"total marks is { tol_marks}")

avg_marks = stu_1 + stu_2 + stu_3 + stu_4 + stu_5 / 5 
print(f"averge marks is { avg_marks} ")

if stu_1 >= stu_2 and stu_1>=stu_3 and stu_1>=stu_4 and stu_1>=stu_5:
    print("student1 has highest marks")
elif stu_2 >= stu_1 and stu_2>=stu_3 and stu_2>=stu_4 and stu_2>=stu_5:
    print("student2 has highest marks")
elif stu_3 >= stu_1 and stu_3>=stu_2 and stu_3>=stu_4 and stu_3>=stu_5:
    print("student3 has highest marks")
elif stu_4 >= stu_1 and stu_4>=stu_2 and stu_4>=stu_3 and stu_4>=stu_5:
    print("student4 has highest marks")
else:
    print("student5 has highest marks")
    
if stu_1 <= stu_2 and stu_1<=stu_3 and stu_1<=stu_4 and stu_1<=stu_5:
    print("student1 has lowest marks")
elif stu_2 <= stu_1 and stu_2<=stu_3 and stu_2<=stu_4 and stu_2<=stu_5:
    print("student2 has lowest marks")
elif stu_3 <= stu_1 and stu_3<=stu_2 and stu_3<=stu_4 and stu_3<=stu_5:
    print("student3 has lowest marks")
elif stu_4 <= stu_1 and stu_4<=stu_2 and stu_4<=stu_3 and stu_4<=stu_5:
    print("student4 has lowest marks")
else:
    print("student5 has lowest marks")
