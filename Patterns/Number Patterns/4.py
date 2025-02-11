#pyramid number 
#      1
#     123
#    12345
#   1234567
#  123456789
n= 5
for i in range(n):
  p = 1
  for j in range(i,n):
    print(" ", end="")
  for j in range (i):
    print(p,end="")
    p+=1
  for j in range (i+1):
    print(p,end="")
    p+=1
  print()