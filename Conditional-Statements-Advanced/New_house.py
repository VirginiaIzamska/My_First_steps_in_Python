
flowers = input()
number_of_flowers = int(input())
budget = int(input())

total_sum = 0

if flowers == 'Roses':
    total_sum = 5.0 * number_of_flowers
    if number_of_flowers > 80:
        total_sum = total_sum * 0.9
elif flowers == 'Dahlias':
    total_sum = 3.80 * number_of_flowers
    if number_of_flowers > 90:
        total_sum = total_sum * 0.85
elif flowers == 'Tulips':
    total_sum = 2.80 * number_of_flowers
    if number_of_flowers > 80:
        total_sum = total_sum * 0.85
elif flowers == 'Narcissus':
    total_sum = 3.0 * number_of_flowers
    if number_of_flowers < 120:
        total_sum += total_sum * 0.15
elif flowers == 'Gladiolus':
    total_sum = 2.50 * number_of_flowers
    if number_of_flowers < 80:
        total_sum += total_sum * 0.20

if budget >= total_sum:
    print(f"Hey, you have a great garden with {number_of_flowers} {flowers} and {abs(budget - total_sum):.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(budget - total_sum):.2f} leva more.")





