# wrong!
print sum([a * 10000 + b * 1000 + c * 100 + d * 10 + e for a in range(10) for b in range(10) for c in range(10) for d in range(10) for e in range(10) if a ** 5 + b ** 5 + c ** 5 + d ** 5 + e ** 5 == a * 10000 + b * 1000 + c * 100 + d * 10 + e]) - 1
