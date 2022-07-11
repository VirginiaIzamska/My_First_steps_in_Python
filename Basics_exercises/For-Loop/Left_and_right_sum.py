n = int(input())

left_sum = 0
right_sum = 0

for _ in range(n):
    left_current_number = int(input())
    left_sum += left_current_number
for _ in range(n):
    right_current_number = int(input())
    right_sum += right_current_number

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(left_sum - right_sum)}")
