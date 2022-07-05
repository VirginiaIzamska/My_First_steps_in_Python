season = input()
type_group = input()
people_number = int(input())
nights_number = int(input())

price_all_nights = 0
type_sport = ''
if season == 'Winter':
    if type_group == 'boys' or type_group == 'girls':
        price_all_nights = 9.60 * nights_number
        if type_group == 'boys':
            type_sport = 'Judo'
        elif type_group == 'girls':
            type_sport = 'Gymnastics'
    elif type_group == 'mixed':
        price_all_nights = 10.00 * nights_number
        type_sport = 'Ski'
elif season == 'Spring':
    if type_group == 'boys' or type_group == 'girls':
        price_all_nights = 7.20 * nights_number
        if type_group == 'boys':
            type_sport = 'Tennis'
        elif type_group == 'girls':
            type_sport = 'Athletics'
    elif type_group == 'mixed':
        price_all_nights = 9.50 * nights_number
        type_sport = 'Cycling'
elif season == 'Summer':
    if type_group == 'boys' or type_group == 'girls':
        price_all_nights = 15.00 * nights_number
        if type_group == 'boys':
            type_sport = 'Football'
        elif type_group == 'girls':
            type_sport = 'Volleyball'
    elif type_group == 'mixed':
        price_all_nights = 20.00 * nights_number
        type_sport = 'Swimming'

if people_number >= 50:
    price_all_nights -= price_all_nights * 0.50
elif people_number >= 20:
    price_all_nights -= price_all_nights * 0.15
elif people_number >= 10:
    price_all_nights -= price_all_nights * 0.05

print(f"{type_sport} {price_all_nights * people_number:.2f} lv.")

