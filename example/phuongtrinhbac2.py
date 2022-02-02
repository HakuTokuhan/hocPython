import math

def phuong_trinh_bac_2(a, b, c):
    x = b*b - 4*a*c

    if a == 0:
        if b == 0:
            print('Phương trình vô nghiệm')
            return
        else:
            print('Phương trình có 1 nghiệm: x = ', -c/b)
            return
    if x > 0:
        x1 = (-b+math.sqrt(x)) / (2*a)
        x2 = (-b-math.sqrt(x)) / (2*a)
        return print('Phương trình có 2 nghiệm phân biệt là: x1 = ', x1,', x2 = ', x2)
    elif x == 0:
        x1 = -b / (2*a)
        return print('Phương trình có nghiệm kép x1 = x2 = ', x1)
    else:
        return print('Phương trình vô nghiệm')

print('ax^2 + bx + c = 0')
a = int(input('Nhap a: '))
b = int(input('Nhap b: '))
c = int(input('Nhap c: '))
phuong_trinh_bac_2(a, b, c)