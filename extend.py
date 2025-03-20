l1=[1,2,3]
print(id(l1))
l2=[2,3,4]
l1=l1+l2
print(id(l1))
print(l1)

l1=[1,2,3]
print(id(l1))
l2=[2,3,4]
l1.extend(l2)
print(id(l1))
print(l1)

#Addition causes formation different id object whereas in extend
# doesn't do