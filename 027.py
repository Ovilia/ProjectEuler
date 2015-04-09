import math


def is_prime(n):
    for i in range(3, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


max_cnt = -1
max_ab = 0
for a in xrange(-999, 1000):
    for b in xrange(-999, 1000):
        cnt = 0
        for n in xrange(1000):
            r = n * n + a * n + b
            if r > 0 and is_prime(r):
                cnt += 1
            else:
                break
        if cnt > max_cnt:
            max_cnt = cnt
            max_ab = a * b
print max_ab
