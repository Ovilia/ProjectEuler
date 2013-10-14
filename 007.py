import math


def is_prime(n):
    for i in range(3, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

cnt = 1
i = 3
while True:
    if is_prime(i):
        cnt += 1
        if cnt == 10001:
            print i
            break
    i += 2
