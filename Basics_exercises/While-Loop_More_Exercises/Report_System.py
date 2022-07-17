collect_sum_sales = int(input())

saved_sum_cash = 0
saved_sum_credit_card = 0
saved_sum = 0
pay_credit_card = 0
pay_cash = 0
count_command = 1
count_cash = 0
count_credit_card = 0
command = input()
while command != 'End' and saved_sum < collect_sum_sales:
    price_items = int(command)
    if count_command % 2 == 0:
        if price_items < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            saved_sum_credit_card += price_items
            saved_sum += price_items
            count_credit_card += 1
    else:
        if price_items > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            saved_sum_cash += price_items
            saved_sum += price_items
            count_cash += 1
    if saved_sum < collect_sum_sales:
        command = input()
        if command == 'End':
            print("Failed to collect required money for charity.")
            break
        count_command += 1

if saved_sum >= collect_sum_sales:
    average_cash = saved_sum_cash / count_cash
    average_credit_card = saved_sum_credit_card / count_credit_card
    print(f"Average CS: {average_cash:.2f}")
    print(f"Average CC: {average_credit_card:.2f}")

