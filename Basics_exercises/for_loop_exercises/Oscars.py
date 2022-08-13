name_actor = input()
points_from_academy = float(input())
number_evaluate_people = int(input())

point_actor = 0.0
for _ in range(number_evaluate_people):
    name_evaluate_people = str(input())
    points_evaluate_people = float(input())
    # length_people = len(name_evaluate_people)
    points_actor = len(name_evaluate_people) * (points_evaluate_people / 2)
    points_from_academy += points_actor

    if points_from_academy > 1250.5:
        print(f"Congratulations, {name_actor} got a nominee for leading role with {points_from_academy:.1f}!")
        break

if points_from_academy <= 1250.5:
    print(f"Sorry, {name_actor} you need {abs(points_from_academy - 1250.5):.1f} more!")
