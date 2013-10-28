def div_sum(n):
    return sum([i for i in range(1, n) if n % i == 0])

s = 0
for i in range(1, 10001):
    j = div_sum(i)
    if j != i:
        if div_sum(j) == i:
            s += i
print s
