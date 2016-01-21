def recurLen(n):
    digits = str(n)
    digitId = 0

    records = []
    remainer = 1
    dividor = n

    while remainer > 0:

        # get next digit if remainer is less than dividor
        while remainer < dividor:
            remainer = remainer * 10

        # check if remainer and dividor pair is in records
        for i in xrange(len(records)):
            (r, d) = records[i]
            if r == remainer and d == dividor:
                # recur, completed
                return len(records) - i

        # push to records
        records.append((remainer, dividor))

        # calculate new remainer
        remainer = remainer - remainer / dividor * dividor

    # remainer is 0, recur length is 0
    return 0



maxLen = 0
maxN = 0

for n in xrange(2, 1001):
    length = recurLen(n)

    if length > maxLen:
        maxLen = length
        maxN = n

print maxN
