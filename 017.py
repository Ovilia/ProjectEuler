single = [3, 3, 5, 4, 4, 3, 5, 5, 4]     # 1 to 9
teen = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]    # 10 to 19
tens = [6, 6, 5, 5, 5, 7, 6, 6]          # 20, 30, 40, ..., 90
hundred = 7                              # 100
thousand = 8                             # 1000
and_ = 3                                 # and

print (sum(single) * 9 + sum(teen) + sum(tens) * 10) * 10 + sum(single) * 100 \
      + hundred * 900 + and_ * 891 + 3 + thousand
