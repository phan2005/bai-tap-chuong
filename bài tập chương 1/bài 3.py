class PS:
    def __init__(self, tu_so, mau_so):
        self.tu_so = tu_so
        self.mau_so = mau_so

    # Phương thức kiểm tra tính hợp lệ của phân số
    def kiem_tra_hop_le(self):
        if self.mau_so == 0:
            return False
        return True

    # Phương thức nhập phân số
    @staticmethod
    def nhap_phan_so():
        tu_so = int(input("Nhập tử số: "))
        mau_so = int(input("Nhập mẫu số: "))
        return PS(tu_so, mau_so)

    # Phương thức in phân số ra màn hình
    def in_phan_so(self):
        if not self.kiem_tra_hop_le():
            print("Phân số không hợp lệ (mẫu số bằng 0).")
        else:
            print(f"Phân số là: {self.tu_so}/{self.mau_so}")

def main():
    # Nhập phân số từ người dùng
    phan_so = PS.nhap_phan_so()

    # Kiểm tra và in phân số
    phan_so.in_phan_so()

if __name__ == "__main__":
    main()