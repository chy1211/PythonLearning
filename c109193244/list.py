a=[1,2,3,4,5]
a.append(65)
a.insert(0,12)
del a[0]
a.remove(65)
for i in a:
    print(i)
for j in range(len(a)):
    print(a[j])
print(a)