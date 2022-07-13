number_loads = int(input())
count_ton_van = 0
count_ton_truck = 0
count_ton_train = 0
average_price_per_ton = 0
count_tonnage = 0
for _ in range(number_loads):
    tonnage = int(input())
    count_tonnage += tonnage
    if tonnage <= 3:
        average_price_per_ton += tonnage * 200
        count_ton_van += tonnage
    elif tonnage <= 11:
        average_price_per_ton += tonnage * 175
        count_ton_truck += tonnage
    elif tonnage >= 12:
        average_price_per_ton += tonnage * 120
        count_ton_train += tonnage

print(f"{average_price_per_ton / count_tonnage:.2f}")
print(f"{count_ton_van / count_tonnage * 100:.2f}%")
print(f"{count_ton_truck / count_tonnage * 100:.2f}%")
print(f"{count_ton_train / count_tonnage * 100:.2f}%")
