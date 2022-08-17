n = int(input())

positive_list = list()
negative_list = list()
for i in range(0, n):
    current_integer = int(input())
    if current_integer >= 0:
        positive_list.append(current_integer)
    else:
        negative_list.append(current_integer)

print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}")
print(f"Sum of negatives: {sum(negative_list)}")
