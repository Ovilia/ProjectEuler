names = sorted(open('022.in', 'r').readline()[1:-1].split('","'))
print sum(i * sum(ord(ch) - ord('A') + 1 for ch in name)
          for i, name in enumerate(names, 1))
