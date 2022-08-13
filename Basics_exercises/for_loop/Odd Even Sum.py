n = int(input())

odd_sum = 0
even_sum = 0

for i in range(n):
    current_number = int(input())
    if i % 2 == 0:
        even_sum += current_number
    else:
        odd_sum += current_number

if even_sum == odd_sum:
    print(f"Yes\nSum = {odd_sum}")
else:
    print(f"No\nDiff = {abs(odd_sum - even_sum)}")
