number = int(input())


for first in range(1, 10):
    sum_left_numbers = 0
    sum_right_numbers = 0
    sum_left_numbers += first
    for second in range(1, 10):
        sum_left_numbers += second
        for third in range(1, 10):
            sum_right_numbers += third
            for fourth in range(1, 10):
                sum_right_numbers += fourth
                if sum_left_numbers == sum_right_numbers:
                    if number % sum_left_numbers == 0:
                        print(f"{first}{second}{third}{fourth}", end=" ")
                else:
                    sum_right_numbers -= fourth

            sum_right_numbers = 0
        sum_left_numbers -= second







