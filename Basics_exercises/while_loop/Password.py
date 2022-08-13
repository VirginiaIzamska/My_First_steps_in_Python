name = input()
password = input()

enter_password = input()
while enter_password != password:
    enter_password = input()

if enter_password == password:
    print(f"Welcome {name}!")


