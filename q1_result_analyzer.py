def analyze_result(name, roll, marks):
    total = sum(marks)
    average = total / len(marks)
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"

    failed_subjects = []
    for j in range(len(marks)):
        if marks[j] < 40:
            failed_subjects.append(f"Subject {j + 1}")
    print(f"Student: {name} (Roll: {roll})")
    print(f"Total: {total}, Average: {average}")
    print(f"Grade: {grade}")
    if failed_subjects:
        print(f"Subjects below 40: {', '.join(failed_subjects)}")
    else:
        print("Subjects below 40: None")
        
name = input()
roll = int(input())
marks = []
for i in range(5):
    marks.append(float(input(f"Enter marks for subject {i + 1}: ")))
analyze_result(name, roll, marks)


