n1 = int(input())
n2 = int(input())
n3 = int(input())

count = 0
current_pin_third = 0
current_pin_second = 0
current_pin_first = 0
is_not_prime = False
for first in range(2, n1+1):
    if first % 2 == 0:
        current_pin_first = first
    else:
        continue
    for second in range(2, n2 + 1):
        count = 0
        for i in range(2, second+1):
            if second % i == 0:
                is_not_prime = True
                count += 1
        if count == 1:
            current_pin_second = second
        elif count > 1:
            continue
        for third in range(2, n3 + 1):

            if third % 2 == 0:
                current_pin_third = third
                print(f"{current_pin_first} {current_pin_second} {current_pin_third}")








