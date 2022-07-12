n = int(input())
max_number = int(input())
sum = max_number
for _ in range(n-1):
    current_element = int(input())
    sum += current_element
    if current_element > max_number:
        max_number = current_element
sum -= max_number

if sum == max_number:
    print(f"Yes\nSum = {max_number}")
else:
    print(f"No\nDiff = {abs(max_number - sum)}")


