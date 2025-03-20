n=[0,1,2,3,4,5,6,7,8,9,10]
i=0
length=len(n) #len function calculates length of list
print(length)

while i<len(n):
    print(n[i])
    i=i+1

n=[0,1,2,3,4,5,6,7,8,9,10]
for i in range(0,len(n),2):
    print(n[i])
