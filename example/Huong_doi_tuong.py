class Circle:
    
    
    def Dientich(self):
        return self.bk * self.bk * 3.141592
    
    
    def Nhap(self):
        self.bk = float(input("Nhập bán kính: "))
        
        
c = Circle()
c.Nhap()
print("Diện tích của hình tròn là:", c.Dientich())



class Circle:
    pi = 3.141592
    
    
    def __init__(self, radius=1):
        self.bk = radius
        
        
    def Dientich(self):
        return self.bk * self.bk * Circle.pi
    
    
c = Circle(5)
print("Diện tích của hình tròn là: ",c.Dientich())



class Student:
    count = 0
    
    
    def __init__(self,id,name):
        self.masv = id
        self.hoten = name
        Student.count = Student.count + 1 #Biến tĩnh
        
        
    def display(self):
        print("Mã sinh viên: %d \nHọ tên: %s" % (self.masv, self.hoten))
        
        
s1 = Student(101,"Trần Hùng")
s2 = Student(102,"Bùi Văn Toản")
s3 = Student(103,"Nguyễn Thị Hoa")
print("Số lượng sinh viên là:", Student.count)
s1.display()
s2.display()
s3.display()



class Phanso:
    
    
    def __init__(self,t=0,m=1):
        self.tu = t
        self.mau = m
        
        
    def nhap(self):
        self.tu = int(input("Nhập tử số: "))
        self.mau = int(input("Nhập mẫu số: "))
        
        
    def inps(self):
        print(self.tu,"/",self.mau)
        
        
    def cong(self,other):
        return Phanso(self.tu*other.mau + self.mau*other.tu,self.mau*other.mau)
    
    
a = Phanso(); b = Phanso(); c = Phanso()
print("Nhập phân số thứ nhất:"); a.nhap()
print("Nhập phân số thứ hai:"); b.nhap()
c = a.cong(b)
print("Tổng của hai phân số là:",end= " ")
c.inps()



class Phanso:
    
    
    def __init__(self,t=0,m=1):
        self.tu = t
        self.mau = m
        
        
    def nhap(self):
        self.tu = int(input("Nhập tử số: "))
        self.mau = int(input("Nhập mẫu số: "))
        
        
    def inps(self):
        print(self.tu,"/",self.mau)
        
        
    def __add__(self,other):
        return Phanso(self.tu*other.mau + self.mau*other.tu,self.mau*other.mau)
    
    
a = Phanso(); b = Phanso(); c = Phanso()
print("Nhập phân số thứ nhất:"); a.nhap()
print("Nhập phân số thứ hai:"); b.nhap()
c = a + b
print("Tổng của hai phân số là:",end= " ")
c.inps()



class Student:
    
    
    def __init__(self, id, name, age):
        self.id = id;
        self.name = name;
        self.age = age
        
        
# tạo đối tượng của lớp Student
s = Student(101, "Trung", 22)
# in thuộc tính name của đối tượng s
print(getattr(s, 'name'))
# gán giá trị của age cho 23
setattr(s, "age", 23)
# in giá trị của age
print(getattr(s, 'age'))
# true nếu student chứa thuộc tính id
print(hasattr(s, 'id'))
# xóa thuộc tính age
delattr(s, 'age')
# phát sinh lỗi nếu age đã bị xóa
print(s.age)



class Chu_nhat:
    
    
    def __init__(self,d,r):
        self.dai = d
        self.rong = r
        
        
    def dientich(self):
        return self.dai * self.rong
    
    
class Vuong(Chu_nhat):
    
    
    def __init__(self,c):
        self.dai = c
        self.rong = c
        
        
cn = Chu_nhat(2,3)
v = Vuong(4)
print("Diện tích hình chữ nhật là: ",cn.dientich())
print("Diện tích hình vuông là: ",v.dientich())