n = int(input())
special_number = 0
for first in range(1, 10):
    for second in range(1, 10):
        for third in range(1, 10):
            for forth in range(1, 10):
                if n % first == 0 and n % second == 0 and n % third == 0 and n % forth == 0:
                    special_number = str(first) + str(second) + str(third) + str(forth)
                    print(special_number, end= " ")
