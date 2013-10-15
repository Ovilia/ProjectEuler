isFound = False
for a in range(1, 1000):
    if isFound:
        break
    for b in range(1, a):
        c = 1000 - a - b
        if a * a + b * b == c * c:
            isFound = True
            print a * b * c
            break
