number_bottles_detergent = int(input())

quantity_detergent = number_bottles_detergent * 750
one_dish = 5
one_pot = 15
used_detergent = 0
count_dishes = 0
count_pots = 0
count_command = 1
command = input()
while command != 'End' and quantity_detergent >= 0:
    number_dishes = int(command)
    if count_command % 3 == 0:
        count_pots += number_dishes
        used_detergent = number_dishes * one_pot
        quantity_detergent -= used_detergent
    else:
        count_dishes += number_dishes
        used_detergent = number_dishes * one_dish
        quantity_detergent -= used_detergent
    if quantity_detergent < 0:
        print(f"Not enough detergent, {abs(quantity_detergent)} ml. more necessary!")
        break
    command = input()
    count_command += 1
else:
    print("Detergent was enough!")
    print(f"{count_dishes} dishes and {count_pots} pots were washed.")
    print(f"Leftover detergent {quantity_detergent} ml.")


