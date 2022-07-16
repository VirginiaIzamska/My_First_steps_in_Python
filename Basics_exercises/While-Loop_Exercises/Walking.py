steps = 0
all_steps = 10000

while steps < 10000:
    steps_per_day = input()
    if steps_per_day == 'Going home':
        steps_per_day = int(input())
        steps += steps_per_day
        if steps >= 10000:
            break
        print(f"{all_steps - steps} more steps to reach goal.")
        break
    steps_per_day = int(steps_per_day)
    steps += steps_per_day

if steps >= all_steps:
    print("Goal reached! Good job!")
    print(f"{steps - all_steps} steps over the goal!")



