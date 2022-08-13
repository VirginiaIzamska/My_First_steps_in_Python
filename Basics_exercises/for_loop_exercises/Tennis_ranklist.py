number_tournament = int(input())
start_points_rank_list = int(input())
add_point = 0
count_winner = 0
for _ in range(number_tournament):
    stage = input()

    if stage == 'W':
        add_point += 2000
        count_winner += 1
    elif stage == 'F':
        add_point += 1200
    elif stage == 'SF':
        add_point += 720
from math import ceil, floor
print(f"Final points: {add_point + start_points_rank_list}")
print(f"Average points: {floor(add_point / number_tournament)}")
print(f"{count_winner / number_tournament * 100:.2f}%")
