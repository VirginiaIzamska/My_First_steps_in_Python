moves_whole_game = int(input())
invalid_numbers = 0
points = 0
count_number_to_10 = 0
count_number_to_20 = 0
count_number_to_30 = 0
count_number_to_40 = 0
count_number_to_50 = 0
count_invalid_number = 0
for _ in range(moves_whole_game):
    current_number = int(input())
    if current_number < 0 or current_number > 50:
        count_invalid_number += 1
        points = points / 2
    elif current_number <= 9:
        points += current_number * 0.20
        count_number_to_10 += 1
    elif current_number <= 19:
        points += current_number * 0.30
        count_number_to_20 += 1
    elif current_number <= 29:
        points += current_number * 0.40
        count_number_to_30 += 1
    elif current_number <= 39:
        points += 50
        count_number_to_40 += 1
    elif current_number <= 50:
        points += 100
        count_number_to_50 += 1


print(f"{points:.2f}")
print(f"From 0 to 9: {count_number_to_10 / moves_whole_game * 100:.2f}%")
print(f"From 10 to 19: {count_number_to_20 / moves_whole_game * 100:.2f}%")
print(f"From 20 to 29: {count_number_to_30 / moves_whole_game * 100:.2f}%")
print(f"From 30 to 39: {count_number_to_40 / moves_whole_game * 100:.2f}%")
print(f"From 40 to 50: {count_number_to_50 / moves_whole_game * 100:.2f}%")
print(f"Invalid numbers: {count_invalid_number / moves_whole_game * 100:.2f}%")


