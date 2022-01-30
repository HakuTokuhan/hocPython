str1 = "Viduhanfind() trong python"
str2 = "find"
print(str1.find(str2))
print(str1.find(str2, 10))
print(str1.find(str2, 20))
print(str1[str1.find(str2):])

str1 ="Vi du Py ham count trong Python, hoc lap trinh Python"
sub = "Py"
print("str1.count(sub, 10): ", str1.count(sub, 10))
print("str1.count(sub, 10, 30): ", str1.count(sub, 10, 30))
sub = "ham"
print("str1.count(sub): ", str1.count(sub))

print("ddd ", len(str1))

str = 'Hello world'
newstr = str.replace('Hello', 'Bye')
print(newstr)

str = "AA BB AA CC AA DD AA EE"
newstr = str.replace('AA', 'aa')
print(newstr)

str = 'AA BB AA CC AA DD AA E'
print(str.split('A'))

str1 = "        Vi du ham lstrip() trong python        "
print(str1.rstrip())
str1 = "--------Vi du ham lstrip() trong python--------"
print(str1.rstrip('-'))

str1 = "hello python"
print(str1.isalpha())
str1 = "hello"
print(str1.isalpha())
str1 = "hello123"
print(str1.isalpha())

lst =[1, 2, 'a', 'b', [3, 4]]
print(lst[0])
print(lst[3])
print(lst[1:3])
print(lst[:2])
print(lst[2:])

lst = [1, 2]
lst += ['one', 'two']
print(lst)
lst += 'addcf213e'
print(lst)
print('------------------------------')

lst = list('KTER') * 3
print(lst)
print([1, 2] * 3)
print('------------------------------')
list1 = ['123', 'abc', 'xyz', 'xzc']
list2 = [222, 333, 1110]
print ("Phan tu co gia tri lon nhat la : ", max(list1))
print ("Phan tu co gia tri lon nhat la : ", max(list2))

aTuple = ('123', 'abc', 'xyz', 'def')
aList = list(aTuple)
print('Cac phan tu cua tuple la: ', aTuple)
print('Cac phan tu cua list la: ', aList)

