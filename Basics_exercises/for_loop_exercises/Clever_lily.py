age_Lili = int(input())
washing_machine_price = float(input())
price_per_toy = int(input())

count_toys = 0
saved_money = 0
count_money = 0
sum_money = 0

for i in range(1, age_Lili + 1):
    if i % 2 == 0:
        saved_money = 10
        count_money += 1
        saved_money *= count_money
        sum_money += saved_money

    else:
        count_toys += 1
sum_money -= count_money * 1
add_money = count_toys * price_per_toy
sum_money += add_money
if washing_machine_price <= sum_money:
    print(f"Yes! {abs(washing_machine_price - sum_money):.2f}")
else:
    print(f"No! {abs(washing_machine_price - sum_money):.2f}")
