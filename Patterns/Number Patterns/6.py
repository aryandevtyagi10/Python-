n = 5
for i in range(n):
  p = 5
  for j in range (i+1):
    print(" ", end ="")
  for j in range (i,n):
    print(p,end ="")
    p -=1
  print()
  