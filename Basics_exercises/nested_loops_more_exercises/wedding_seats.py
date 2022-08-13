last_sector = input()
number_rows_first_sector = int(input())
number_odd_seats = int(input())

current_even_seats = 0
current_rows = number_rows_first_sector
counter_all_seats = 0
for sectors in range(65, ord(last_sector) + 1):
    for rows in range(1, current_rows + 1):
        if rows % 2 != 0:
            counter_all_seats += number_odd_seats
            for seats in range(97, number_odd_seats + 97):
                print(f"{chr(sectors)}{rows}{chr(seats)}")

        else:
            current_even_seats = number_odd_seats + 2
            counter_all_seats += current_even_seats
            for seats in range(97, current_even_seats + 97):
                print(f"{chr(sectors)}{rows}{chr(seats)}")

    current_rows += 1

print(counter_all_seats)