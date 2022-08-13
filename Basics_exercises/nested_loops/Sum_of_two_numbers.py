first_num = int(input())
second_num = int(input())
magic_num = int(input())

combinations = 0
count_all_combinations = 0
for i in range(first_num, second_num + 1):
    for j in range(first_num, second_num + 1):
        sum = i + j
        count_all_combinations += 1
        if sum == magic_num:
            combinations += 1
            print(f"Combination N:{count_all_combinations} ({i} + {j} = {magic_num})")
            break
    if sum == magic_num:
        break


if combinations == 0:
    print(f"{count_all_combinations} combinations - neither equals {magic_num}")

