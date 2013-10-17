import math


def factor_cnt(n):
    cnt = 2  # 1 and n
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            cnt += 2
    return cnt - 1 if int(math.sqrt(n)) ** 2 == n else cnt

n = 2
test = 1
while True:
    test = n + test
    n += 1
    if factor_cnt(test) > 500:
        print test
        break
