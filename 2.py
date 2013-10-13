def fab(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
        yield b

max = 4000000
f = fab(max)
n = f.next()
sum = 0
while True:
    n = f.next()
    if n > max:
        break
    if n % 2 == 0:
        sum += n
print sum