n=[1,2,3,4,5,6]
for i in n:
    print(i)

for i in range(0,len(n)):
    print(n[i])



n=[[1],[2,3],[4,5,6]]
for i in n:
    print(i)


for i in range(0,len(n)):
    for j in range(0,len(n[i])):
        print(n[i][j])