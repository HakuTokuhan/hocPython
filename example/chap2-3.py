print('Lap trinh python')

a = 200
print('Gia tri: ', a, 'gffg')

print("Xin chào các bạn sinh viên")
print("Khoa CNTT")
print("Xin chào các bạn sinh viên",end = "\t\t")
print("Khoa CNTT")

print(230, 250)
print(230, 250, sep= '[[[')
print(230, 250, 123, sep='+', end='\n')
print(230, 250, 123, sep='+', end='!')

a = 100
b = 200
print('Gia tri cua a la: {} va b la: {}'.format(a,b))


print('Gia tri cua a la: {0} va b la: {1}'.format(a,b))
print('Gia tri cua a la: {1} va b la: {0}'.format(a,b))

print("Lap tring {lang} {prop}".format(lang = 'python', prop = 'co ban'))

a = 100.50
print('Gia tri la %.2f' %a)

print("Ten toi la %s va toi nang %d kg" %('Hoang', 71))

a = 7.0
b = 2
print('%f/%d = %f' %(a, b, a/b))
print('%6.1f/%4d = %6.1f' %(a, b, a/b))

list1 = ['java', 'python', 'c++']
print ("Phan tu cua list truoc khi them : ", list1)
list1.append('php')
print ("Phan tu cua list sau khi them : ", list1)

list1 = ['java', 'python', 'c++', 'python']
print("So lan 'python' xuat hien trong List la : ", list1.count('python'))
print("So lan 'java' xuat hien trong List la : ", list1.count('java'))

list1 = ['java', 'python', 'c++']
list2 = ['c++', 'sql']
list1.extend(list2)
print('List sau khi duoc mo rong them la: ', list1)

list1 = ['java', 'python', 'c++', 'php', 'sql']
print("Chi muc cua 'python' la: ", list1.index('python'))
print("chi muc cua 'php' la: ", list1.index('php'))

list1 = ['java', 'python', 'c++', 'php', 'sql']
list1.insert(3, 'android')
print("List sau khi duoc mo rong la: ", list1)

list1 = ['java', 'python', 'c++', 'php', 'sql']
list1.pop()
print("List: ", list1)
list1.pop(2)
print("List: ", list1)

list1 = ['java', 'python', 'c++', 'php', 'sql']
list1.remove('c++')
print('List: ', list1)
list1.remove('java')
print('List:', list1)

fruits = ["apple", "banana", "guava"]
del fruits[0]
print(fruits)

list1 = ['java', 'python', 'c++', 'php', 'sql']
list1.reverse()
print('List bi dao nguoc: ', list1)

fruits = ["apple", "banana", "guava"]
fruits.clear()
print(fruits)

list.sort([reverse])

vowels = ['e', 'a', 'u', 'o', 'i']
print("Truoc khi sap xep: ",vowels)
vowels.sort()
print("Sau khi sap xep tang dan: ",vowels)
vowels.sort(reverse=True)
print("Sau khi sap xep giam dan: ",vowels)

lst = [[1, 2, 3], [4, 5, 6]]
print(lst)
