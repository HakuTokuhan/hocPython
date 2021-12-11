a = 4

print(a)

print(type(a))

b = 1.123456789101112131415

print(b)

print(type(b))

# lấy toàn bộ thư viện decimal
from decimal import*1

# lấy tối đa 30 chữ só phần nguyên và phần thập phân Decimal
getcontext().prec = 30

f = 10/3
print(f)

d = Decimal(10)/Decimal(3)
print(d)
