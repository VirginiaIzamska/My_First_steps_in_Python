n = int(input())

list = []
filtered = []
flag = False
for i in range(0, n):
    current_integer = int(input())
    list.append(current_integer)
command = input()

if command == 'even':
    for number in list:
        if number % 2 == 0:
            filtered.append(number)
elif command == 'odd':
    for number in list:
        if number % 2 != 0:
            filtered.append(number)
elif command == 'negative':
    for number in list:
        if number < 0:
            filtered.append(number)
elif command == 'positive':
    for number in list:
        if number >= 0:
            filtered.append(number)

print(filtered)


