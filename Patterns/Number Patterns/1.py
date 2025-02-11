#increasing triangle
n = 5
p = 1
for i in range (n):
  for j in range (i+1):
    # print(i+1,end ="") #alternate method
    print(p,end ="")
  p+=1 #p-=1 or p+=2 any variation acc. to question
  print()

  # output:
  # 1
  # 22
  # 333
  # 4444
  # 55555
