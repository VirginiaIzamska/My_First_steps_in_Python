city = input()
volume_sales = float(input())

discount = 0
if 0 <= volume_sales <= 500:
    if city == 'Sofia':
        discount = volume_sales * 0.05
    elif city == 'Varna':
        discount = volume_sales * 0.045
    elif city == 'Plovdiv':
        discount = volume_sales * 0.055
elif volume_sales <= 1000:
    if city == 'Sofia':
        discount = volume_sales * 0.07
    elif city == 'Varna':
        discount = volume_sales * 0.075
    elif city == 'Plovdiv':
        discount = volume_sales * 0.08
elif volume_sales <= 10000:
    if city == 'Sofia':
        discount = volume_sales * 0.08
    elif city == 'Varna':
        discount = volume_sales * 0.10
    elif city == 'Plovdiv':
        discount = volume_sales * 0.12
elif volume_sales > 10000:
    if city == 'Sofia':
        discount = volume_sales * 0.12
    elif city == 'Varna':
        discount = volume_sales * 0.13
    elif city == 'Plovdiv':
        discount = volume_sales * 0.145

if volume_sales < 0 or city not in 'Sofia Plovdiv Varna':
    print('error')
else:
    print(f'{discount:.2f}')
