""""
while True:
    H, W = [int(i) for i in input().split()]
    if H == w == 0:
        break

    for i in range(H):
        for w in range(W):
            print('#',end='')

        print('#', end='')

    print()

print()
"""
"""
while True:
    h, w = map(int,input().strip().split())
    if h == w == 0: berak
    for y in range(h):
        print(''.join('#.'[(x + y) % 2] for x in range(w)))
    print()
"""

"""
while True:
    (H, W) = [int(i) for i in input().split()]
    if H == W == 0:
        break
    print('#' * W)
    for a in range(H-2):
        print('#'+'.'*(W-2)+'#')
    print('#' * W)
    print('')
"""
"""
input()
a = input().split()
a.reverse()
for b in a:
    print(b, end='_')
"""
"""
data = [
    "{0} {1}".format(s, r)
    for s in ('S', 'H', 'C', 'D')
    for r in range(1, 13 + 1)
]
count = int(input())
for c in range(count):
    card = input()
    data.remove(card)

print("\n".join(data))
"""
'''
data = [
    [[0 for r in range(10)]for f in range(3)] for b in range(4)
]

# 入力データ読み込んで処理をここから書いていく
count = int(input())
for c in range(count):
    b, f, r, v = [int(i) for i in input().split()]
    data[b-1[f-1][r-1] += v

for b in enumerate(data):
    for f in b:
        for r in f:
            print(' {0}'.format(r), end='')

        print()

    if bi < 3:
    　　print('#'* 20)
'''

'''
n, m = [int(i) for i in input().split()]

matrix = []
for ni in range(n):
    matrix.append([int(a) for a in input().split()])

vector = []
for mi in range(m):
    vector.append(int(input()))



for ni in range(n):
    sum = 0
    for mi in range(m):
        sum += matrix[ni][mi] * vector[mi]


print(sum)

'''
'''
while True:
    m, f, r = [int(i) for i in input().split()]

    if m == f == r == -1:
        break

    total = m + f
    if m == -1 or f == -1 or total< 30:
        print('F')

    elif total < 50 anfd r < 50:
        print('D')

    elif total < 65:
        print('C')

    elif total < 80:
        print('B')

    else:
        print('A')
'''
'''
import time


class Timer(object):
    def __int__(self, verbose=False):
        self.verbose = verbose

    def __enter__(self):
        self._start__time = time.time()
        return  self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._end__time = time.time()
        self.secs = self._end__time - self._start__time
        self.millis = self.secs * 1000
        if self.verbose:
            print('elapasd time: {0:f} ms'.format(self.millis))
'''

'''
r, c = [int(i) for i in input().split()]

data = []
sum_row = [0] * (c + 1)

for ri in range(r):
    data.append([int(i) for i in input().split()])
    data[ri].append(sum(data[ri]))
    print(" ".join([str(d) for d in data[ri]]))
    for ci in range(c + 1):
        sum_row[ci] += data[ri][ci]

print(" ".join([str(s) for s in sum_row]))
'''
'''
n, m, l = [int(i) for i in input().split()]

A = []
B = []
C = []

for ni in range(n):
    A.append([int(i) for i in input().split()])

for mi in range(m):
    B.append([int(i) for i in input().split()])

for i in range(n):
    C.append([])
    for j in range(l):
        C[i].append(0)
        for k in range(m):
            C[i][j] += A[i][k] * B[k][j]

for li in range(l):
    print(" ".join([str(s) for s in C[ni]]))
'''

'''print(input().swapcase())'''

'''
import string

count = {x: 0 for x in string.ascii_lowercase}
lines = ""

while True:
    try:
        lines += input().lower()
    except EOFError:
        break

for c in lines:
    if 'a' <= c <= 'z':
        count[c] += 1

for key in string.ascii_lowercase:
    print("{0} : {1}".format(key, count[key]))
'''

s = input()
q = int(input())

for qi in range(q):
    command = input().split()

    a = int(command[1])
    b = int(command[2])
    if command[0] == 'print':
       print(s[a:b +1])
    elif command[0] == 'reverse':
        s = s[:a] + reversed[a:b + 1][::-1] + s[b + 1]
    else:
        p = command[3]
        