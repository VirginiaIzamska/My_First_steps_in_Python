months = input()
number_nights = int(input())

studio = 0
apartment = 0

if months == 'May' or months == 'October':
    studio = 50.0
    apartment = 65.0
    if number_nights > 14:
        studio = studio * 0.70
    elif number_nights > 7:
        studio = studio * 0.95
elif months == 'June' or months == 'September':
    studio = 75.20
    apartment = 68.70
    if number_nights > 14:
        studio = studio * 0.80
elif months == 'July' or months == 'August':
    studio = 76.00
    apartment = 77.00

if number_nights > 14:
    apartment = apartment * 0.90

print(f"Apartment: {apartment * number_nights:.2f} lv.")
print(f"Studio: {studio * number_nights:.2f} lv.")
