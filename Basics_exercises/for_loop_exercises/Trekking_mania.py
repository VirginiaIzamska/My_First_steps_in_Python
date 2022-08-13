number_group_climbers = int(input())
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0
count_people = 0
for _ in range(number_group_climbers):
    number_people_in_each_group = int(input())
    count_people += number_people_in_each_group
    if number_people_in_each_group <= 5:
        musala += number_people_in_each_group
    elif number_people_in_each_group <= 12:
        monblan += number_people_in_each_group
    elif number_people_in_each_group <= 25:
        kilimandjaro += number_people_in_each_group
    elif number_people_in_each_group <= 40:
        k2 += number_people_in_each_group
    elif number_people_in_each_group >= 41:
        everest += number_people_in_each_group

musala = musala / count_people * 100
monblan = monblan / count_people * 100
kilimandjaro = kilimandjaro / count_people * 100
k2 = k2 / count_people * 100
everest = everest / count_people * 100

print(f'{musala:.2f}%')
print(f'{monblan:.2f}%')
print(f'{kilimandjaro:.2f}%')
print(f'{k2:.2f}%')
print(f'{everest:.2f}%')

