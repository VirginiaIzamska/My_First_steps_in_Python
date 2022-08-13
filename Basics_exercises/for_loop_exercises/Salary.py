tabs_open_browser = int(input())
salary = int(input())
fine = 0
for _ in range(tabs_open_browser):
    website_name = input()
    if website_name == 'Facebook':
        fine += 150
    elif website_name == 'Instagram':
        fine += 100
    elif website_name == 'Reddit':
        fine += 50
    if fine >= salary:
        print("You have lost your salary.")
        break
if salary > fine:
    print(abs(salary - fine))
