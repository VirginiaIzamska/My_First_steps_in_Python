
budget = int(input())
season = input()
number_fishmen = int(input())
ship_price = 0

if season == 'Spring':
    ship_price = 3000
    if number_fishmen <= 6:
        ship_price = ship_price * 0.90
    elif number_fishmen <= 11:
        ship_price = ship_price * 0.85
    elif number_fishmen >= 12:
        ship_price = ship_price * 0.75
elif season == 'Summer' or season == 'Autumn':
    ship_price = 4200
    if number_fishmen <= 6:
        ship_price = ship_price * 0.90
    elif number_fishmen <= 11:
        ship_price = ship_price * 0.85
    elif number_fishmen >= 12:
        ship_price = ship_price * 0.75
elif season == 'Winter':
    ship_price = 2600
    if number_fishmen <= 6:
        ship_price = ship_price * 0.90
    elif number_fishmen <= 11:
        ship_price = ship_price * 0.85
    elif number_fishmen >= 12:
        ship_price = ship_price * 0.75

if number_fishmen % 2 == 0 and season != 'Autumn':
    ship_price -= ship_price * 0.05

if budget >= ship_price:
    print(f"Yes! You have {abs(budget - ship_price):.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(budget - ship_price):.2f} leva.")


