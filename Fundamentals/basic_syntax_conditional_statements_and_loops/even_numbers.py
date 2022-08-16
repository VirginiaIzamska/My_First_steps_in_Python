n = int(input())
flag = False
for i in range(1, n + 1):
    current_number = int(input())
    if current_number % 2 != 0:
        flag = True
        print(f"{current_number} is odd!")
        break
if not flag:
    print("All numbers are even.")

