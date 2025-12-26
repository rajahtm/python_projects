from operations import adddata,delate_data,viewdata
print(" 1 add data")
print("2 delate data")
print("3 view data")
print("4 update data")
print("5 exit")
choice = int(input("enter your choice:"))
if choice ==1:
    student_name = input("enter student name:")
    student_age = int(input("enter student age:"))
    student_address = input("enter student address:")
    adddata(student_name, student_age, student_address)
elif choice ==2:
    studentage = int(input("enter student age to delate data:"))
    delate_data(studentage)
elif choice ==3:
    print("viewing data from database:")
    tablename = input("enter table name :")
    viewdata(tablename)