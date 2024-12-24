# Lớp Đa giác
class DaGiac:
    def __init__(self, so_canh=0):
        self.so_canh = so_canh

    def nhap(self):
        self.so_canh = int(input("Nhập số cạnh của đa giác: "))

    def in_thong_tin(self):
        print(f"Đa giác có {self.so_canh} cạnh.")

# Lớp Hình Bình Hành (kế thừa từ Đa Giác)
class HinhBinhHanh(DaGiac):
    def __init__(self, canh_day=0, chieu_cao=0):
        super().__init__(4)  # Hình bình hành có 4 cạnh
        self.canh_day = canh_day
        self.chieu_cao = chieu_cao

    def nhap(self):
        self.canh_day = float(input("Nhập chiều dài cạnh đáy: "))
        self.chieu_cao = float(input("Nhập chiều cao: "))

    def tinh_dien_tich(self):
        return self.canh_day * self.chieu_cao

    def in_thong_tin(self):
        super().in_thong_tin()
        print(f"Hình bình hành có cạnh đáy: {self.canh_day} và chiều cao: {self.chieu_cao}")
        print(f"Diện tích: {self.tinh_dien_tich()}")

# Lớp Hình Chữ Nhật (kế thừa từ Hình Bình Hành)
class HinhChuNhat(HinhBinhHanh):
    def __init__(self, chieu_dai=0, chieu_rong=0):
        super().__init__(chieu_dai, chieu_rong)
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def nhap(self):
        self.chieu_dai = float(input("Nhập chiều dài: "))
        self.chieu_rong = float(input("Nhập chiều rộng: "))

    def tinh_chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)

    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong

    def in_thong_tin(self):
        super().in_thong_tin()
        print(f"Hình chữ nhật có chiều dài: {self.chieu_dai}, chiều rộng: {self.chieu_rong}")
        print(f"Chu vi: {self.tinh_chu_vi()}")
        print(f"Diện tích: {self.tinh_dien_tich()}")

# Lớp Hình Vuông (kế thừa từ Hình Chữ Nhật)
class HinhVuong(HinhChuNhat):
    def __init__(self, canh=0):
        super().__init__(canh, canh)

    def nhap(self):
        canh = float(input("Nhập độ dài cạnh hình vuông: "))
        self.chieu_dai = self.chieu_rong = canh

    def in_thong_tin(self):
        print(f"Hình vuông có cạnh: {self.chieu_dai}")
        print(f"Chu vi: {self.tinh_chu_vi()}")
        print(f"Diện tích: {self.tinh_dien_tich()}")

# Chương trình chính
print("Chọn loại hình cần nhập:")
print("1. Hình bình hành")
print("2. Hình chữ nhật")
print("3. Hình vuông")
choice = int(input("Lựa chọn của bạn: "))

if choice == 1:
    hbh = HinhBinhHanh()
    hbh.nhap()
    hbh.in_thong_tin()

elif choice == 2:
    hcn = HinhChuNhat()
    hcn.nhap()
    hcn.in_thong_tin()

elif choice == 3:
    hv = HinhVuong()
    hv.nhap()
    hv.in_thong_tin()

else:
    print("Lựa chọn không hợp lệ.")