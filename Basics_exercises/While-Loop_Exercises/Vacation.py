money_trip = float(input())
current_money = float(input())

count_spend_money = 0
saved_money = 0
spend_money = 0
count_days = 0
while True:
    if current_money >= money_trip:
        print(f"You saved the money for {count_days} days.")
        break
    command = input()
    sum_save_or_spend = float(input())
    count_days += 1
    if command == 'save':
        saved_money = sum_save_or_spend
        current_money += saved_money
        count_spend_money = 0
    elif command == 'spend':
        if current_money >= spend_money:
            spend_money = sum_save_or_spend
            if spend_money > current_money:
                current_money = 0
            else:
                current_money -= spend_money
        count_spend_money += 1
        if count_spend_money == 5:
            print("You can't save the money.")
            print(f"{count_days}")
            break

# if current_money >= money_trip:
#     print(f"You saved the money for {count_days} days.")

