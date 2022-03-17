obj=open("abcd.txt","w")
obj.write("Python xin chao cac ban")
obj.close()

a = []
n = int(input("Nhập số phần tử của dãy số:"))
for i in range(1,n+1):
k = int(input("Nhập phần tử thứ " + str(i) + ":"))
a.append(k)
obj=open("e:\\dulieu.txt","w")
for i in a:
obj.write(str(i) + " ")
obj.close()

m = int(input("Nhập số hàng = "))
n = int(input("Nhập số cột = "))
a = []
for i in range(0, m):
a.append([])
for j in range(0, n):
x = float(input("Nhap phan tu thu a[%2d][%2d]: " % (i+1, j+1)))
a[i].append(x)
obj=open("e:\\matran.txt","w")
obj.write("Mang vua nhap la: \n")
for i in range(0, m):
for j in range(0, n):
obj.write(str(a[i][j]) + " ")
obj.write("\n")
obj.close()

f = open("e:\\toanco.txt","r")
l = f.readline()
while l:
print(l)
l = f.readline()

f = open("e:\\toanco.txt","r")
for l in f:
print(l)

fo = open("foo.txt", "w")
fo.write("Python la mot ngon ngu lap trinh tuyet
voi.\nMinh cung nghi nhu the!!\n")
fo.close()

fo = open("foo.txt", "w")
print ("Ten cua file la: ", fo.name)
print ("File da duoc dong hay chua : ",
fo.closed)
print ("Che do truy cap la : ", fo.mode)

import os
os.rename( "foo.txt", "test2.txt" )

import os
os.remove("text2.txt")

fo = open("foo.txt", "r+")
str = fo.read(10)
print ("Chuoi da doc la : ", str)
position = fo.tell()
print ("Con tro file hien tai : ", position)
position = fo.seek(0, 0)
str = fo.read(10)
print ("Chuoi da doc la : ", str)
fo.close()

import os
os.mkdir("test")

import os
# Thay doi mot thu muc toi "/Bai giang/Python"
os.chdir("/Bai giang/Python")

import os
# Lenh nay se cung cap vi tri thu muc hien tai
os.getcwd()

import os
# Xoa thu muc "/tmp/test".
os.rmdir( "/tmp/test" )