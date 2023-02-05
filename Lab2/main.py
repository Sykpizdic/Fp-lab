def print_student_info(name, age, grade):
    print("Student name:", name)
    print("Student age:", age)
    print("Student grade:", grade)

# Input student information
name = input("Enter student name: ")
age = int(input("Enter student age: "))
grade = int(input("Enter student grade: "))

# Check grade and print appropriate message
if grade >= 90:
    print("Excellent performance!")
elif grade >= 80:
    print("Good job!")
else:
    print("Keep working hard!")

# Call function to print student information
print_student_info(name, age, grade)