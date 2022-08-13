width_cake = int(input())
height_cake = int(input())

all_cake = width_cake * height_cake
pieces_cake_left = all_cake
each_piece_of_cake = input()
while each_piece_of_cake != 'STOP' and pieces_cake_left > 0:
    each_piece_of_cake = int(each_piece_of_cake)
    pieces_cake_left -= each_piece_of_cake
    if pieces_cake_left <= 0:
        print(f"No more cake left! You need {abs(pieces_cake_left)} pieces more.")
        break
    each_piece_of_cake = input()

if pieces_cake_left > 0:
    print(f"{pieces_cake_left} pieces are left.")
