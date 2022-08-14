high_border_100 = int(input())
high_border_10 = int(input())
high_border_1 = int(input())

flag = False
counter = 0
first_number = 0
second_number = 0
third_number = 0

for first in range(2, high_border_100 + 1):
    if first % 2 == 0:
        first_number = first
    else:
        continue
    for second in range(2, high_border_10 + 1):
        counter = 0
        for i in range(2, second+1):
            if second % i == 0:
                flag = True
                counter += 1
        if counter == 1:
            second_number = second
        elif counter > 1:
            continue
        for third in range(2, high_border_1 + 1):
            if third % 2 == 0:
                third_number = third
                print(f"{first_number} {second_number} {third_number}")
