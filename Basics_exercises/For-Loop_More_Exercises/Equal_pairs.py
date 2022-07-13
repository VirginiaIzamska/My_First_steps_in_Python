import sys

n = int(input())

n1 = int(input())
n2 = int(input())
first_value = n1 + n2
second_value = 0
diff = 0
max_diff = -sys.maxsize
for i in range(1, n):
    n1 = int(input())
    n2 = int(input())
    current_value = n1 + n2
    if i % 2 == 0:
        first_value = current_value
    else:
        second_value = n1 + n2
    if first_value != second_value:
        diff = abs(first_value - second_value)
        if max_diff < diff:
            max_diff = diff

if first_value == second_value or n < 2:
    print(f"Yes, value={first_value}")
else:
    print(f"No, maxdiff={max_diff}")

