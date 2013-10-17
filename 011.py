n = 20

grid = []
infile = open('011.in', 'r')
for i in range(n):
    grid.append([int(i) for i in infile.readline()[:-1].split(' ')])

product = 1
for i in range(n - 3):
    for j in range(n - 3):
        product = max(product,
                grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j],
                grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3],
                grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2]
                * grid[i + 3][j + 3], grid[i + 3][j] * grid[i + 2][j + 1]
                * grid[i + 1][j + 2] * grid[i][j + 3])
    for j in range(n - 3, n):
        product = max(product,
                grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j],
                grid[j][i] * grid[j][i + 1] * grid[j][i + 2] * grid[j][i + 3])
print product
