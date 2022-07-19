symbols = input()

word = ''
count_special_c = 0
count_special_o = 0
count_special_n = 0
special_word = 0
while symbols != 'End':
    if symbols != "c" and symbols != "o" and symbols != "n":
        if chr(65) <= symbols <= chr(90) or chr(97) <= symbols <= chr(122):
            word += symbols
    elif symbols == 'c':
        count_special_c += 1
        if count_special_c == 1:
            special_word += 1
        else:
            word += symbols
    elif symbols == 'o':
        count_special_o += 1
        if count_special_o == 1:
            special_word += 1
        else:
            word += symbols
    elif symbols == 'n':
        count_special_n += 1
        if count_special_n == 1:
            special_word += 1
        else:
            word += symbols
    if special_word == 3:
        print(word, end=' ')
        count_special_c = 0
        count_special_n = 0
        count_special_o = 0
        word = ''
        special_word = 0
    symbols = input()





