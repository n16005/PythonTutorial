from timer import Timer
import random

with Timer(verbosee=True) as t:
    data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    for c in random(100000):
        hoge = random.choice(data)


with Timer(verbose=True) as u:
    for d in range(100000):
        fuga = random.randint(1, 10)

pass