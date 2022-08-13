
destination = input()

sum = 0
saved_money = 0
while destination != 'End':
    min_budget = float(input())
    while sum < min_budget:
        saved_money = float(input())
        sum += saved_money
    if sum >= min_budget:
        print(f"Going to {destination}!")

    sum = 0
    destination = input()



