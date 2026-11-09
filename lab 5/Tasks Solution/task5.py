student={
    "Student names":"Marks",
    "Student 1":90,
    "Student 2":80,
    "Student 3":50,
}   
print("A — Add a student")
print("B — Update student marks")
print("C — Search for a student")
print("D — Display all students and marks")

choice=input("Enter the choice: ")
if choice=="A"or choice=="B"or choice=="C"or choice=="D":

    if choice=="A":
        student_name=input("Enter the student name: ")
        marks=int(input("Enter the marks: "))
        
        student.update({student_name:marks})
        print("Added successfully")

    elif choice== "B":
        student_name=input("Enter the student name: ")
        if student_name in student:
            marks=int(input("Enter the updated marks: "))
            print("Updated Successfully")
        else:
            print("This student is not in dictionary!")

    elif choice=="C":
        search=input("Enter student name: ")
        if search in student:
            print("Marks: ",student[search])
        else:
            print("Student not found")
    elif choice=="D":
        print(student)
else:   
    print("Invalid")
