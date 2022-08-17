first_string = input() #tail
second_string = input() # body
third_string = input() # head

meerkats = list()

meerkats.append(first_string)
meerkats.append(second_string)
meerkats.append(third_string)

meerkats[2], meerkats[0] = meerkats[0], meerkats[2]
print(meerkats)

