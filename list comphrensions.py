squares=[x*x for x in range(5)]
print(squares)

numbers = [10, 12, 23, 14, 15] 
squared = [x ** 2 for x in numbers]
print(squared)

List = [character for character in [1, 2, 3]] 
print(List)

list = [i for i in range(11) if i % 2 == 0] 
print(list)

list = [i for i in range(11) if i % 2 == 0] 
print(list)

N = 5
arr = [0 for i in range(N)]
print(arr) 

matrix = [[j for j in range(3)] for i in range(3)] 
print(matrix)


matrix = [[0 for j in range(3)] for i in range(3)] 
print(matrix)

s=[x*x for x in range(1,11)]
print(s)
v=[2**x for x in range(1,6)]
print(v)
m=[x for x in s if x%2==0]
print(m)

country=["America","India","China","Japan","France","England","Spain"]
l=[w[0] for w in country]
print(l)

n1=[1,2,3,4,5]
n2=[4,5,6,7,8]
n3=[i for i in n1 if i not in n2]
n4=[i for i in n1 if i in n2]
print(n3)
print(n4)

str="KIET group of Institutions"
l=[[w.upper(),len(w)] for w in str.split()]
print(l)
