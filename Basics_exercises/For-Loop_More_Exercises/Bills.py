months_average_cost = int(input())
water = 0
internet = 0
others = 0
others_cost = 0
electricity = 0
average_costs = 0
for _ in range(months_average_cost):
    electricity_bill = float(input())
    electricity += electricity_bill
    others += 20 + 15 + electricity_bill
    others += others * 0.20
    others_cost += others
    others = 0
water = 20 * months_average_cost
internet = 15 * months_average_cost
average_costs = electricity + others_cost + water + internet
print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {others_cost:.2f} lv")
print(f"Average: {average_costs/ months_average_cost:.2f} lv")

