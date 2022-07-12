number_students_in_exam = int(input())

top_students = 0
fail_students = 0
students_less_five_grade = 0
students_less_three_grade = 0
average_success = 0
for _ in range(number_students_in_exam):
    grade_per_student = float(input())
    average_success += grade_per_student
    if grade_per_student >= 5.00:
        top_students += 1
    elif grade_per_student >= 4.00:
        students_less_five_grade += 1
    elif grade_per_student >= 3.00:
        students_less_three_grade += 1
    elif grade_per_student < 3.00:
        fail_students += 1

print(f"Top students: {top_students / number_students_in_exam * 100:.2f}%")
print(f"Between 4.00 and 4.99: {students_less_five_grade / number_students_in_exam * 100:.2f}%")
print(f"Between 3.00 and 3.99: {students_less_three_grade / number_students_in_exam * 100:.2f}%")
print(f"Fail: {fail_students / number_students_in_exam * 100:.2f}%")
print(f"Average: {average_success / number_students_in_exam:.2f}")



