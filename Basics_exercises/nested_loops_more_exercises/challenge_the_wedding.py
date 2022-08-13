men_number = int(input())
women_number = int(input())
table_number = int(input())


for men in range(1, men_number+1):
    count_table = 0
    count_table += 1
    for women in range(1, women_number+1):
        count_table += 1
        table_number -= 1
        if table_number < 0:
            break
        print(f"({men} <-> {women})", end=" ")
        count_table -= 1
    if table_number < 0:
        break
