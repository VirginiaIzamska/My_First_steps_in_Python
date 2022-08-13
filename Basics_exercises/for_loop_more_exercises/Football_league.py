capacity_of_stadium = int(input())
number_fens = int(input())

fens_A = 0
fens_B = 0
fens_V = 0
fens_G = 0
for _ in range(1, number_fens + 1):
    area = input()
    if area == 'A':
        fens_A += 1
    elif area == 'B':
        fens_B += 1
    elif area == 'V':
        fens_V += 1
    elif area == 'G':
        fens_G += 1

print(f"{fens_A / number_fens * 100:.2f}%")
print(f"{fens_B / number_fens * 100:.2f}%")
print(f"{fens_V / number_fens * 100:.2f}%")
print(f"{fens_G / number_fens * 100:.2f}%")
print(f"{(fens_G+fens_A+fens_V+fens_B) / capacity_of_stadium * 100:.2f}%")
