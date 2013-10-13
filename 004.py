def is_palindrome(n):
    s = str(n)
    for i in range(len(s) / 2):
        if s[i] != s[-i - 1]:
            return False
    return True

big = -1
for i in range(100, 1000):
    for j in range(100, 1000):
        p = i * j
        if p > big and is_palindrome(p):
            big = p
print(big)
