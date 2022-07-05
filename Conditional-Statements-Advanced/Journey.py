budget = float(input())
season = input()

destination = ''
holiday = ''
if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        budget = budget * 0.30
        holiday = 'Camp'
    elif season == 'winter':
        budget = budget * 0.70
        holiday = 'Hotel'
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        budget = budget * 0.40
        holiday = 'Camp'
    elif season == 'winter':
        budget = budget * 0.80
        holiday = 'Hotel'
elif budget > 1000:
    destination = 'Europe'
    budget = budget * 0.90
    holiday = 'Hotel'

print("Somewhere in " + destination)
print(f"{holiday} - {budget:.2f}")
