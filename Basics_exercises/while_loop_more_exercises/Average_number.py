n = int(input())

sum = 0
for _ in range(1, n + 1):
    current_number = int(input())
    sum += current_number

average_sum = sum / n
print(f"{average_sum:.2f}")
