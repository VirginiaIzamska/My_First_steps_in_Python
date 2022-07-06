hour_exam = int(input())
minutes_exam = int(input())
hour_arrive = int(input())
minutes_arrive = int(input())

hour_exam_mins = hour_exam * 60
hour_arrive_mins = hour_arrive * 60
minutes_exam = minutes_exam + hour_exam_mins
minutes_arrive = minutes_arrive + hour_arrive_mins
total_hour = 0
total_mins = 0
difference = abs(minutes_arrive - minutes_exam)
if minutes_exam < minutes_arrive:
    print("Late")
    if minutes_arrive - minutes_exam < 60:
        print(f"{difference} minutes after the start")
    else:
        total_mins = difference % 60
        total_hour = difference // 60
        if total_mins < 10:
            print(f"{total_hour:.0f}:0{total_mins} hours after the start")
        else:
            print(f"{total_hour:.0f}:{total_mins} hours after the start")
elif minutes_exam == minutes_arrive or (minutes_exam - minutes_arrive <= 30):
    print("On time")
    if minutes_exam != minutes_arrive:
        print(f"{difference} minutes before the start")
elif minutes_exam - minutes_arrive > 30:
    print("Early")
    if minutes_exam - minutes_arrive < 60:
        print(f"{difference} minutes before the start")
    else:
        total_mins = difference % 60
        total_hour = difference // 60
        if total_mins < 10:
            print(f"{total_hour:.0f}:0{total_mins} hours before the start")
        else:
            print(f"{total_hour:.0f}:{total_mins} hours before the start")

