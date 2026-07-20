# report.py

def create_report(name, score):
    print("----- Report -----")
    print("Name:", name)
    print("Score:", score)

    if score >= 50:
        print("Status: Pass")
    else:
        print("Status: Fail")

# Main program
student_name = input("Enter name: ")
student_score = int(input("Enter score: "))

create_report(student_name, student_score)
