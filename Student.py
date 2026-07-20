students = []

# Add students
name = input("Enter student name: ")
age = int(input("Enter student age: "))
grade = input("Enter student grade: ")

student = {
    "name": name,
    "age": age,
    "grade": grade
}

students.append(student)

# Display students
print("\nStudent Details")
print("----------------")
for s in students:
    print("Name:", s["name"])
    print("Age:", s["age"])
    print("Grade:", s["grade"])
