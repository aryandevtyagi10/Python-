# 1
# 22
# 111
# 2222
# 11111

n = 5
for i in range(n):
  for j in range(i+1):
    if (i%2 == 0):
      print('1',end="")
    else:
      print('2',end ="")
  print()