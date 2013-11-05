def fab(n):
    a = 0
    b = 1
    i = 0
    while i < n:
        a, b = b, a + b
        yield b
        ++i

f = fab(10 ** 1000)
n = f.next()
m = 0
while True:
    n = f.next()
    print n
    m += 1
    if len(str(n)) >= 1000:
        print m
        break
