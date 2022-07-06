days = int(input())
room = input()
valuation = input()

price_per_night = 0
sum = 0

if room == 'room for one person':
    price_per_night = 18.00
    sum = price_per_night * (days - 1)
elif room == 'apartment':
    price_per_night = 25.00
    sum = price_per_night * (days - 1)
    if days < 10:
        sum -= sum * 0.30
    elif days <= 15:
        sum -= sum * 0.35
    elif days > 15:
        sum -= sum * 0.50
elif room == 'president apartment':
    price_per_night = 35.00
    sum = price_per_night * (days - 1)
    if days < 10:
        sum -= sum * 0.10
    elif days <= 15:
        sum -= sum * 0.15
    elif days > 15:
        sum -= sum * 0.20

discount = 0
if valuation == 'positive':
    discount = sum * 0.25
    sum += discount
else:
    discount = sum * 0.10
    sum -= discount

print(f'{sum:.2f}')


