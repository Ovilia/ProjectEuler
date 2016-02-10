def next_pos(x, y, direction):
    if direction == 0:
        x += 1
    elif direction == 1:
        y += 1
    elif direction == 2:
        x -= 1
    elif direction == 3:
        y -= 1
    else:
        assert False
    return x, y


size = 1001
arr = [[0 for w in xrange(size)] for h in xrange(size)]

x = size - 1
y = 0
direction = 2  # 0: right, 1: down, 2: left, 3: top

# write from outside to inside
for i in xrange(size * size, 0, -1):
    arr[y][x] = i

    nextX, nextY = next_pos(x, y, direction)

    # change direction if meet border or already existing number
    if nextX < 0 or nextX >= size or nextY < 0 or nextY >= size or arr[nextY][nextX] != 0:
        if direction == 0:
            direction = 3
        else:
            direction -= 1
        x, y = next_pos(x, y, direction)
    else:
        x, y = nextX, nextY

res = -1
for i in xrange(size):
    res += arr[i][i] + arr[i][size - 1 - i]

print res