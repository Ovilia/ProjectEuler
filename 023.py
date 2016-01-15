import math
from sets import Set

def sumOfDiv(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1

    s = 1
    for i in xrange(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            s += i
            if i * i != n:
                s += n / i
    return s



maxSum = 28123

# set of abundant numbers
abSet = Set()
for i in xrange(1, maxSum):
    s = sumOfDiv(i)
    if s > i:
        # is abundant
        abSet.add(i)

# set of numbers can be presented as sum of two abundant numbers
sumSet = Set()
for i in abSet:
    for j in abSet:
        if i + j <= maxSum:
            sumSet.add(i + j)

print (1 + maxSum) * maxSum / 2 - sum(sumSet)
