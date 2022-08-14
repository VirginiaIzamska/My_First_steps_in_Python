#
import itertools

a = 5

for i in itertools.cycle(1, a+1):
    print(i)
