
sum_prime_number = 0
sum_non_prime_number = 0
command = input()
is_flag = False
while command != 'stop':
    current_num = int(command)
    if current_num < 0:
        print("Number is negative.")
    else:
        for i in range(2, current_num):
            if current_num % i == 0:
                is_flag = True
                sum_non_prime_number += current_num
                break
            else:
                is_flag = False
        if not is_flag:
            sum_prime_number += current_num

    command = input()

print(f"Sum of all prime numbers is: {sum_prime_number}")
print(f"Sum of all non prime numbers is: {sum_non_prime_number}")
