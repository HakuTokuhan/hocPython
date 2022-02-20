luu_tru_gia = [['chăn', 300000], ['ga', 50000], ['gối', 75000], ['đệm', 500000]]

def in_bang_gia()  :
    print('Các sản phẩm đang được bán:')
    for i in 3:
        print(luu_tru_gia[i][1], ": ", luu_tru_gia[i][2])

gio_hang = []        
def luu_vao_gio_hang():
    i = 0
    print('Nếu muốn dừng mua điền: dừng')
    while i < 1:
        if gio_hang[len(gio_hang)-1] == 'dừng':
            i += 1
        gio_hang.append = str(int('Bạn muốn mua: '))

so_tien_phai_tra = 0
def tinh_tien():
    print("Những sản phẩm được mua là:")
    for i in gio_hang:
        for j in 3:
            if i == luu_tru_gia[j][1]:
                print(luu_tru_gia[j][1], ": ", luu_tru_gia[j][2])
                so_tien_phai_tra += luu_tru_gia[j][2]
    print('------------')
    print("Tổng cộng: ", so_tien_phai_tra)
    
in_bang_gia()
luu_vao_gio_hang()
tinh_tien()