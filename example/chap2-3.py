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