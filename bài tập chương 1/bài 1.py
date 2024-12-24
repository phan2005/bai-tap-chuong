# định nghĩa hình chứ nhât
class HinhChuNhat:
    def __init__(self,chieu_dai,chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
    def tinh_chu_vi(self):
        return 2*(self.chieu_dai + self.chieu_rong)
    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong
#nhap dữ liệu
chieu_dai = float(input("nhập chiều dài:"))
chieu_rong = float(input("nhập chiều rộng"))
#tạo đối tượng 
hinh_chu_nhat = HinhChuNhat(chieu_dai,chieu_rong)
print(f"chu vi cua hinh chu nhat là :{hinh_chu_nhat.tinh_chu_vi()}")
print(f"dien tich cua hinh chu nhat là :{hinh_chu_nhat.tinh_dien_tich()}")
