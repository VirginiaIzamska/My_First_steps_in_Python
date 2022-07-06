degrees = int(input())
part_of_time = input()

outfit = ''
shoes = ''
if 10 <= degrees <= 18:
    if part_of_time == 'Morning':
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif part_of_time == 'Afternoon' or part_of_time == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
elif 18 < degrees <= 24:
    if part_of_time == 'Morning' or part_of_time == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif part_of_time == 'Afternoon':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
elif degrees >= 25:
    if part_of_time == 'Morning':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif part_of_time == 'Afternoon':
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
    elif part_of_time == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'

print(f"It's {degrees:.0f} degrees, get your {outfit} and {shoes}.")

