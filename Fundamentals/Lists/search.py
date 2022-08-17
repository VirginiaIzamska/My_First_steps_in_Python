n = int(input())
word = input()
strings = list()
second_string = []
for i in range(0, n):
    current_string = input()
    strings.append(current_string)
    if word in current_string:
        second_string.append(current_string)

print(strings)
print(second_string)
