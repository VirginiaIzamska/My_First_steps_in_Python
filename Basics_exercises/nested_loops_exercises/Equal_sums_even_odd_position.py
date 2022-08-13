first_num = int(input())
second_num = int(input())

for first in range(first_num, second_num + 1):
    current_num = str(first)
    odd_sum = 0
    even_sum = 0
    for i, digit in enumerate(current_num):
        if i % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    if odd_sum == even_sum:
        print(current_num, end=" ")
