n = int(input())
count_p1 = 0
count_p2 = 0
count_p3 = 0
count_p4 = 0
count_p5 = 0
for _ in range(n):
    current_num = int(input())
    if current_num < 200:
        count_p1 += 1
    elif 399 >= current_num >= 200:
        count_p2 += 1
    elif 599 >= current_num >= 400:
        count_p3 += 1
    elif 799 >= current_num >= 600:
        count_p4 += 1
    elif current_num >= 800:
        count_p5 += 1

p1 = count_p1 / n * 100
p2 = count_p2 / n * 100
p3 = count_p3 / n * 100
p4 = count_p4 / n * 100
p5 = count_p5 / n * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")
