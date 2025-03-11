tuple=(1,2,3,4,5,6)
tuple2=(1,2,3,[10,20,30],40)


print(tuple[1])
tuple[1]=10

print(tuple2[3])
print(tuple2[3][1])
tuple2[3][1]=200
print(tuple2)


