n = int(input())
count = 0
for row in range(1, n+1):
    for cols in range(1, row + 1):
        if count == n:
            break
        count += 1
        print(count, end=" ")
    if count == n:
        break
    print()


