width_size = int(input())
height_size = int(input())
length_size = int(input())

all_apartment_volume = width_size * height_size * length_size
all_space = 0

command = input()
while (command != 'Done') and (all_space < all_apartment_volume):
    number_box = int(command)
    all_space += number_box
    if all_apartment_volume > all_space:
        command = input()

if all_apartment_volume >= all_space:
    print(f"{all_apartment_volume - all_space} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(all_apartment_volume - all_space)} Cubic meters more.")
