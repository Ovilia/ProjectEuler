import math

total = 2
n = 3
while True:
    found = True
    for i in xrange(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            found = False
            break
    if found:  # is a prime
        if n > 2000000:
            print total
            break
        else:
            total += n
    n += 2

