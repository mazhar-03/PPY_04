students = [
 {"name": "Alice", "exam_score": 85, "attendance": 90},
 {"name": "Bob", "exam_score": 58, "attendance": 75},
 {"name": "Charlie", "exam_score": 45, "attendance": 80},
 {"name": "Diana", "exam_score": 92, "attendance": 95},
 {"name": "Ethan", "exam_score": 60, "attendance": 40}
]


def evaluate(name):
    found = False
    for student in students:
        if student["name"] == name:
            found = True
            passed_score = student["exam_score"] >= 60
            passed_attendance = student["attendance"] >= 50
            if passed_attendance and passed_score:
                print(f"{student["name"]} has PASSED the class!\n")
            else:
                print(f"{student["name"]} has FAILED the class!\n")
    if not found:
        print("The student is not found.\n")


while True:
    student_name = input("Enter student name, for exit press 0: ")
    if student_name == "0":
        print("Exiting...")
        break
    evaluate(student_name)

