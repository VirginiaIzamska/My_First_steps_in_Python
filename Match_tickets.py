budget = float(input())
category = input()
number_people = int(input())

if 1 <= number_people <= 4:
    budget -= budget * 0.75
elif number_people <= 9:
    budget -= budget * 0.60
elif number_people <= 24:
    budget -= budget * 0.50
elif number_people <= 49:
    budget -= budget * 0.40
elif number_people >= 50:
    budget -= budget * 0.25

ticket_price_VIP = 499.99
ticket_price_Normal = 249.99
sum_ticket = 0
if category == "VIP":
    sum_ticket = ticket_price_VIP * number_people
    if sum_ticket <= budget:
        print(f"Yes! You have {abs(sum_ticket - budget):.2f} leva left.")
    else:
        print(f"Not enough money! You need {abs(sum_ticket - budget):.2f} leva.")
elif category == "Normal":
    sum_ticket = ticket_price_Normal * number_people
    if sum_ticket <= budget:
        print(f"Yes! You have {abs(sum_ticket - budget):.2f} leva left.")
    else:
        print(f"Not enough money! You need {abs(sum_ticket - budget):.2f} leva.")
