chrysanthemum_number = int(input())
roses_number = int(input())
tulip_number = int(input())
season = input()
holiday_day = input()

chrysanthemum_price = 0
roses_price = 0
tulip_price = 0
if season == 'Spring' or season == 'Summer':
    chrysanthemum_price = chrysanthemum_number * 2.00
    roses_price = roses_number * 4.10
    tulip_price = tulip_number * 2.50
elif season == 'Winter' or season == 'Autumn':
    chrysanthemum_price = chrysanthemum_number * 3.75
    roses_price = roses_number * 4.50
    tulip_price = tulip_number * 4.15

total_price = 0
if holiday_day == 'Y':
    total_price = chrysanthemum_price + roses_price + tulip_price
    total_price += total_price * 0.15
else:
    total_price = chrysanthemum_price + roses_price + tulip_price

if tulip_number > 7 and season == 'Spring':
    total_price -= total_price * 0.05
elif roses_number >= 10 and season == 'Winter':
    total_price -= total_price * 0.10
if (chrysanthemum_number + roses_number + tulip_number) > 20:
    total_price -= total_price * 0.20

print(f"{(total_price + 2):.2f}")


