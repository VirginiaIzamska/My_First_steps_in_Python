junior_number = int(input())
senior_number = int(input())
trace = input()

tax_juniors = 0
tax_seniors = 0
total_tax = 0
if trace == 'trail':
    tax_juniors = junior_number * 5.50
    tax_seniors = senior_number * 7.0
    total_tax = tax_juniors + tax_seniors
elif trace == 'cross-country':
    tax_juniors = junior_number * 8.00
    tax_seniors = senior_number * 9.50
    total_tax = tax_juniors + tax_seniors
    if (junior_number + senior_number) >= 50:
        total_tax -= total_tax * 0.25
elif trace == 'downhill':
    tax_juniors = junior_number * 12.25
    tax_seniors = senior_number * 13.75
    total_tax = tax_juniors + tax_seniors
elif trace == 'road':
    tax_juniors = junior_number * 20.00
    tax_seniors = senior_number * 21.50
    total_tax = tax_juniors + tax_seniors

total_tax -= total_tax * 0.05

print(f"{total_tax:.2f}")
