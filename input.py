x=input("Enter nos")
print(type(x))

x=int(input("Enter nos"))
print(type(x))

x,y = [int(x) for x in input("Enter two values: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)

x,y,z = [int(x) for x in input("Enter three values: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)
print("Second Number is: ", z)

x = [int(x) for x in input("Enter two values: ").split()]
print("First Number is: ", x)
