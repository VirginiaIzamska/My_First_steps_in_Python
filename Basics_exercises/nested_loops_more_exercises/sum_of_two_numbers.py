start_number = int(input())
end_number = int(input())
magic_number = int(input())

counter = 0
flag = False
for first in range(start_number, end_number+1):
    sum = 0
    for second in range(start_number, end_number+1):
        sum = first + second
        counter += 1
        if sum == magic_number:
            flag = True
            print(f"Combination N:{counter} ({first} + {second} = {magic_number})")
            break
        sum -= second
    if flag:
        break

if not flag:
    print(f"{counter} combinations - neither equals {magic_number}")
