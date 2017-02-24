end = 100

s = set()
for a in range(2, end + 1):
    for b in range(2, end + 1):
        s.add(a ** b)
print len(s)
