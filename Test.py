a = [1,2,3,4,5]

j = 0
for i in range(2, 0, -1):
    i = i * (-1)
    print(i)
    a.insert(j, a.pop(i))
    print(a)
    j += 1




    b.pop(i)
    b[0] = c

print(a,b)


b = a.copy()
a.pop(-2)
a[0]= 9