n = int(input())
total_avg_score = 0
count_grades = 0

current_grade = 0
text = input()
while text != 'Finish':
    score = 0
    avg_score = 0
    current_grade = 0
    for _ in range(n):
        grade = float(input())
        score += grade
        current_grade += 1
        count_grades += 1

    total_avg_score += score
    avg_score = score / current_grade
    print(f"{text} - {avg_score:.2f}.")
    text = input()

total_avg_score = total_avg_score / count_grades
print(f"Student's final assessment is {total_avg_score:.2f}.")
