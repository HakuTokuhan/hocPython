tup = [1, 2]
tup +=('Hello','World')
print(tup)

tup = tuple('abc') * 3
print(tup)
print((1,) * 0)
print((1,) * 3)

print(1 in (1, 2, 3))
print(4 in (1, 2, 'Hello', 'World'))

tup = ((1, 2, 3), [4, 5])
print(tup[0])
print( tup[0][2])
print( tup[1][0])

tup = (1, 5, 3, 5, 6, 1, 1)
print(tup.count(1))
print(tup.count(4))

tup=('a','b','c')
print( tup.index('b'))
