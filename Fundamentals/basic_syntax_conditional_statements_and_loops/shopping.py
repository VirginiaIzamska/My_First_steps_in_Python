budjet = int(input())


command = input()
budjet_left = budjet
flag = False
while command != 'End':
    current_price = int(command)
    budjet_left -= current_price
    if budjet_left < 0:
        flag = True
        print("You went in overdraft!")
        break
    command = input()

if not flag:
    print("You bought everything needed.")