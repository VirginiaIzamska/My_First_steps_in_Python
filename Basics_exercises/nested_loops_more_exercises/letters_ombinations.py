first_letter = input()
second_letter = input()
third_letter = input()
#
# biggest_letter = max(ord(first_letter), ord(second_letter), ord(third_letter))
# smallest_letter = min(ord(first_letter), ord(second_letter), ord(third_letter))
count_combination = 0
for first in range(ord(first_letter), ord(second_letter) + 1):
    for second in range(ord(first_letter), ord(second_letter) + 1):
        for third in range(ord(first_letter), ord(second_letter) + 1):
            if chr(third) != third_letter and chr(second) != third_letter and chr(first) != third_letter:
                print(f"{chr(first)}{chr(second)}{chr(third)}", end=' ')
                count_combination += 1

print(count_combination)
