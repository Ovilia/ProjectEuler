def collatz_step(n):
    i = 1
    while n != 1:
        n = n / 2 if n % 2 == 0 else 3 * n + 1
        i += 1
    return i

steps = 1
n = 1
for i in range(1, 1000000):
    c = collatz_step(i)
    if c > steps:
        steps = c
        n = i
print n
