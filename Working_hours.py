
part_of_day_and_night = int(input())
day_of_week = str(input())

# 10-18 часа,

if 18 >= part_of_day_and_night >= 10:
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday' or day_of_week == 'Friday' or day_of_week == 'Saturday':
        print('open')
    else:
        print('closed')
else:
    print('closed')
