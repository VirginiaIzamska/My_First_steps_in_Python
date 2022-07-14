name_student = input()

graduated_class = 1
total_grade = 0
bad_grade = 0

while graduated_class <= 12 and bad_grade != 2:
    current_grade = float(input())
    if current_grade >= 4.0:
        total_grade += current_grade
        graduated_class += 1
    else:
        bad_grade += 1

if bad_grade == 2:
    print(f"{name_student} has been excluded at {graduated_class} grade")
else:
    average_grade = total_grade / 12
    print(f"{name_student} graduated. Average grade: {average_grade:.2f}")




