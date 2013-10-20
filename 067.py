infile = open('067.in')
lines = []
for line in infile:
    lines.append([int(i) for i in line[:-1].split(' ')])

route = lines[-1]
for i in range(len(lines) - 1, 0, -1):
    for j in range(i):
        route[j] = max(route[j], route[j + 1]) + lines[i - 1][j]

print route[0]
