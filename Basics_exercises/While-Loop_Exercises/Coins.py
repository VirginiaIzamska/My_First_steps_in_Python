from math import ceil
change = float(input())
change *= 100
count_coins = 0
coins_two_lev = 200
coins_one_lev = 100
coins_fifty = 50
coins_twenty = 20
coins_ten = 10
coins_five = 5
coins_two = 2
coins_one = 1

while change > 0:
    if change >= coins_two_lev:
        count_coins += 1
        change -= coins_two_lev
    elif change >= coins_one_lev:
        count_coins += 1
        change -= coins_one_lev
    elif change >= coins_fifty:
        count_coins += 1
        change -= coins_fifty
    elif change >= coins_twenty:
        count_coins += 1
        change -= coins_twenty
    elif change >= coins_ten:
        count_coins += 1
        change -= coins_ten
    elif change >= coins_five:
        count_coins += 1
        change -= coins_five
    elif change >= coins_two:
        count_coins += 1
        change -= coins_two
    elif change >= coins_one:
        count_coins += 1
        change -= coins_one
print(count_coins)
