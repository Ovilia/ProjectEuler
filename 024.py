import itertools
print ''.join(str(x) for x in list(itertools.permutations(range(10)))[999999])
