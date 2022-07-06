type_projection = input()
number_rows = int(input())
number_columns = int(input())

ticket_price = 0
total_places = number_rows * number_columns
if type_projection == 'Premiere':
    ticket_price = 12.0
    ticket_price *= total_places
    print(f'{ticket_price:.2f} leva')
elif type_projection == 'Normal':
    ticket_price = 7.50
    ticket_price *= total_places
    print(f'{ticket_price:.2f} leva')
elif type_projection == 'Discount':
    ticket_price = 5.00
    ticket_price *= total_places
    print(f'{ticket_price:.2f} leva')
