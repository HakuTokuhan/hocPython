try:
    a = int(input("Nhập vào a:"))
    b = int(input("Nhập vào b:"))
    print("Kết quả %d / %d = %f" %(a,b,a/b))
except ZeroDivisionError:
    print("Không thể chia cho số 0")


try:
    a = int(input("Nhập vào a:"))
    b = int(input("Nhập vào b:"))
    print("Kết quả %d / %d = %f" %(a,b,a/b))
except ZeroDivisionError as e:
    print("Lỗi: ",str(e))


try:
    a = int(input("Nhập vào a:"))
    b = int(input("Nhập vào b:"))
    print("Kết quả %d / %d = %f" %(a,b,a/b))
except:
    print("Không thể chia cho số 0")
    

f = open('integers.txt', 'w')
f.write('12 345 abc\n')
f.close()
try:
    f = open('integers.txt')
    s = f.readline()
    i = int(s.strip())
    print("Số đọc được là: ",i)
except (IOError, ValueError):
    print ("Lỗi vào/ra hoặc sai kiểu dữ liệu")
except:
    print ("Một lỗi nào đó đã xảy ra")


f = open('integers.txt', 'w')
f.write('12')
f.close()
try:
    f = open('integers.txt')
    s = f.readline()
    i = int(s.strip())
    print("Số đọc được là: ",i)
except (IOError, ValueError):
    print ("Lỗi vào/ra hoặc sai kiểu dữ liệu")
except:
    print ("Một lỗi nào đó đã xảy ra")
    

try:
    f = open("testfile", "w")
    f.write("Day la mot kiem tra nho ve xu ly ngoai le!!")
except IOError:
    print("Error: Khong tim thay file")
else:
    print("Da ghi noi dung vao file")
finally:
    f.close()
    

try:
    age = int(input("Nhập số tuổi:"))
    if(age < 18):
        raise ValueError
    else:
        print("số tuổi hợp lệ")
except ValueError:
    print("số tuổi không hợp lệ")



try:
    a = int(input("Nhập vào a:"))
    b = int(input("Nhập vào b:"))
    if b is 0:
        raise ArithmeticError
    else:
        print("a/b = ",a/b)
except ArithmeticError:
    print("Giá trị của b không thể bằng 0")



try:
    x = int(input("Nhập vào một tháng: "))
    if x<1 or x>12:
        raise Exception
    if x in [1,2,3]:
        print("Quý 1")
    elif x in [4,5,6]:
        print("Quý 2")
    elif x in [7,8,9]:
        print("Quý 3")
    else:
        print("Quý 4")
except:
    print ("Bạn nhập sai tháng!")
    

try:
    num = int(input("Nhập một số nguyên dương: "))
    if(num <= 0):
        raise ValueError("Đây là một số âm!")
except ValueError as e:
    print(e)
    
    

try:
    a = int(input("Nhập một số nguyên dương nhỏ hơn 100: "))
    #sinh lỗi khi số quá bé
    if a <= 0:
        raise ValueError ("Bạn đã nhập một số quá nhỏ")
    #sinh lỗi khi số quá lớn
    if a > 100:
        raise ValueError ("Bạn cần nhập số nhỏ hơn 100")
    print("Bạn đã nhập số nằm trong khoảng [1, 100]")
except ValueError as ex:
    print(ex)
