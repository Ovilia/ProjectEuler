nList = []
infile = open('013.in', 'r')
for i in range(100):
    nList.append(int(infile.readline()))
print str(sum(nList))[:10]