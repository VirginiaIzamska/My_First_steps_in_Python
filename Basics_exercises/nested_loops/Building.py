number_floor = int(input())
number_room_per_floor = int(input())

offices = "O"
large_apartments = "L"
apartments = "A"
for floor in range(number_floor, 0, -1):
    for room in range(0, number_room_per_floor):
        if floor == number_floor:
            print(f"{large_apartments}{floor}{room}", end=" ")
        elif floor % 2 == 0:
            print(f"{offices}{floor}{room}", end=" ")
        else:
            print(f"{apartments}{floor}{room}", end=" ")

    print()
