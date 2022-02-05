def sum(a, b):
    return (a+b)

def giaithua(m):
    gt = 1
    for i in range(1,m+1):
        gt = gt*i
    return gt
n = int(input("Nhập vào một số nguyên dương: "))
print("%d! = %d" %(n,giaithua(n)))

def sum(a, b = 10):
    return (a+b)
print(sum(1,2))
print(sum(5))

nhan_doi = lambda a: a * 2
print(nhan_doi(10))

list_goc = [10, 9, 8, 7, 6, 1, 2, 3, 4, 5]
list_moi = list(filter(lambda a: (a%2 == 0) , list_goc))
print(list_moi)

list_goc = [10, 9, 8, 7, 6, 1, 2, 3, 4, 5]
list_moi = list(map(lambda a: a*2 , list_goc))
print(list_moi)