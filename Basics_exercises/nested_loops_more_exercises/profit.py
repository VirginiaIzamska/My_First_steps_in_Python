coins_one_lev = int(input())
coins_two_lev = int(input())
money_five_lev = int(input())
sum = int(input())

total = 0

one_lev = 1
two_lev = 2
five_lev = 5
for i in range(0, coins_one_lev + 1):
    count_one_lev = 0
    count_two_lev = 0
    count_five_lev = 0
    if i > 0:
        count_one_lev += 1
    i = i * one_lev
    for j in range(0, coins_two_lev + 1):
        if j > 0:
            count_two_lev += 1
        j = j * two_lev
        for k in range(0, money_five_lev + 1):
            if k > 0:
                count_five_lev += 1
            k = k * five_lev
            total = i + j + k
            if total == sum:
                print(f"{count_one_lev} * 1 lv. + {count_two_lev} * 2 lv. + {count_five_lev} * 5 lv. = {sum} lv.")

