bad_grade = int(input())

message = input()
count_bad_grade = 0
count_tasks = 0
last_task = ""
total_grade = 0
count_grade = 0
while message != 'Enough':
    grade = int(input())
    count_grade += 1
    if grade <= 4:
        count_bad_grade += 1
        if count_bad_grade == bad_grade:
            print(f"You need a break, {bad_grade} poor grades.")
            break
    total_grade += grade
    count_tasks += 1
    last_task = message
    message = input()

else:
    avg_score = total_grade / count_grade
    print(f"Average score: {avg_score:.2f}")
    print(f"Number of problems: {count_tasks}")
    print(f"Last problem: {last_task}")
