class TS:
    Diem_chuan = 20
    def __init__(self):
        self.danh_sach_thi_sinh = []
    def nhap_thi_sinh(self):
        ho_ten = input("Nhập họ tên thí sinh: ")
        toan = float(input("Nhập điểm Toán: "))
        ly = float(input("Nhập điểm Lý: "))
        hoa = float(input("Nhập điểm Hóa: "))
        tong_diem = toan + ly + hoa
        self.danh_sach_thi_sinh.append({
            'ho_ten': ho_ten,
            'toan': toan,
            'ly': ly,
            'hoa': hoa,
            'tong_diem': tong_diem
        })

    def nhap_danh_sach_thi_sinh(self):
        so_luong = int(input("Nhập số lượng thí sinh: "))
        for _ in range(so_luong):
            self.nhap_thi_sinh()

    def in_thi_sinh(self, thi_sinh):
        print(f"Họ tên: {thi_sinh['ho_ten']}, Toán: {thi_sinh['toan']}, Lý: {thi_sinh['ly']}, Hóa: {thi_sinh['hoa']}, Tổng điểm: {thi_sinh['tong_diem']}")

    def in_danh_sach_thi_sinh(self):
        for thi_sinh in self.danh_sach_thi_sinh:
            self.in_thi_sinh(thi_sinh)

    def loc_va_sap_xep_thi_sinh(self):
        danh_sach_trung_tuyen = [thi_sinh for thi_sinh in self.danh_sach_thi_sinh if thi_sinh['tong_diem'] >= self.Diem_chuan]
        danh_sach_trung_tuyen.sort(key=lambda x: x['tong_diem'], reverse=True)
        return danh_sach_trung_tuyen

    def in_danh_sach_trung_tuyen(self):
        danh_sach_trung_tuyen = self.loc_va_sap_xep_thi_sinh()
        print(f"\nDanh sách thí sinh trúng tuyển (điểm chuẩn = {self.Diem_chuan}):")
        for thi_sinh in danh_sach_trung_tuyen:
            self.in_thi_sinh(thi_sinh)

def main():
    # Tạo đối tượng TS để quản lý thí sinh
    ts = TS()

    # Bước 1: Nhập danh sách thí sinh
    ts.nhap_danh_sach_thi_sinh()

    # Bước 2: In danh sách tất cả thí sinh
    print("\nDanh sách thí sinh:")
    ts.in_danh_sach_thi_sinh()

    ts.in_danh_sach_trung_tuyen()

if __name__ == "__main__":
    main()