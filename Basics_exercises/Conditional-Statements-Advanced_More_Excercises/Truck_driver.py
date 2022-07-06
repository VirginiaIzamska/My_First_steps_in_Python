season = input()
kilometers_per_month = float(input())

salary = 0
sum_per_month = 0
if season == 'Spring' or season == 'Autumn':
    if kilometers_per_month <= 5000:
        sum_per_month = kilometers_per_month * 0.75
        salary = sum_per_month * 4
    elif kilometers_per_month <= 10000:
        sum_per_month = kilometers_per_month * 0.95
        salary = sum_per_month * 4
elif season == 'Summer':
    if kilometers_per_month <= 5000:
        sum_per_month = kilometers_per_month * 0.90
        salary = sum_per_month * 4
    elif kilometers_per_month <= 10000:
        sum_per_month = kilometers_per_month * 1.10
        salary = sum_per_month * 4
elif season == 'Winter':
    if kilometers_per_month <= 5000:
        sum_per_month = kilometers_per_month * 1.05
        salary = sum_per_month * 4
    elif kilometers_per_month <= 10000:
        sum_per_month = kilometers_per_month * 1.25
        salary = sum_per_month * 4
if 10000 < kilometers_per_month <= 20000:
    sum_per_month = kilometers_per_month * 1.45
    salary = sum_per_month * 4

salary -= salary * 0.10

print(f'{salary:.2f}')

