
product = str(input())
town = str(input())
quantity = float(input())

price = 0
if product == 'coffee':
    if town == 'Sofia':
        price = 0.50 * quantity
    elif town == 'Plovdiv':
        price = 0.40 * quantity
    elif town == 'Varna':
        price = 0.45 * quantity
elif product == 'water':
    if town == 'Sofia':
        price = 0.80 * quantity
    elif town == 'Plovdiv' or town == 'Varna':
        price = 0.70 * quantity
elif product == 'beer':
    if town == 'Sofia':
        price = 1.20 * quantity
    elif town == 'Plovdiv':
        price = 1.15 * quantity
    elif town == 'Varna':
        price = 1.10 * quantity
elif product == 'sweets':
    if town == 'Sofia':
        price = 1.45 * quantity
    elif town == 'Plovdiv':
        price = 1.30 * quantity
    elif town == 'Varna':
        price = 1.35 * quantity
elif product == 'peanuts':
    if town == 'Sofia':
        price = 1.60 * quantity
    elif town == 'Plovdiv':
        price = 1.50 * quantity
    elif town == 'Varna':
        price = 1.55 * quantity

print(f'{price}')
