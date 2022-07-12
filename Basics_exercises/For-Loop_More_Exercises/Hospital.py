period_of_time = int(input())

doctors = 7
treated_patients = 0
untreated_patients = 0
for i in range(1, period_of_time + 1):
    number_patients = int(input())
    if i % 3 == 0:
        if treated_patients < untreated_patients:
            doctors += 1
    if number_patients <= doctors:
        treated_patients += number_patients
    else:
        treated_patients += doctors
        untreated_patients += number_patients - doctors

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")


