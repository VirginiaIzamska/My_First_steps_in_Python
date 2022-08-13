film_name = input()
standard_ticket = 0
student_ticket = 0
kid_ticket = 0
total_tickets = 0
while film_name != 'Finish':
    free_places = int(input())
    current_free_places = free_places
    ticket_type = ''
    busy_places = 0
    command = input()
    while command != 'End' and free_places != 0:
        ticket_type = command
        if ticket_type == 'standard':
            standard_ticket += 1
        elif ticket_type == 'student':
            student_ticket += 1
        elif ticket_type == 'kid':
            kid_ticket += 1
        busy_places += 1
        total_tickets += 1
        free_places -= 1
        if free_places == 0:
            break
        command = input()
    avg_score = busy_places / current_free_places * 100
    print(f"{film_name} - {avg_score:.2f}% full.")

    film_name = input()


avg_student_tickets = student_ticket / total_tickets * 100
avg_standard_tickets = standard_ticket / total_tickets * 100
avg_kid_tickets = kid_ticket / total_tickets * 100
print(f"Total tickets: {total_tickets}")
print(f"{avg_student_tickets:.2f}% student tickets.")
print(f"{avg_standard_tickets:.2f}% standard tickets.")
print(f"{avg_kid_tickets:.2f}% kids tickets.")
