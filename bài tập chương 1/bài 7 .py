class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        """In ra thông tin về ngày, tháng, năm."""
        print(f"{self.day:02d}/{self.month:02d}/{self.year}")

    def next(self):
        """Tính ngày tiếp theo và cập nhật."""
        # Số ngày của mỗi tháng (tháng 2 có thể có 28 hoặc 29 ngày)
        days_in_month = [31, 29 if self.is_leap_year(self.year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Kiểm tra nếu đã hết tháng
        if self.day < days_in_month[self.month - 1]:
            self.day += 1
        else:
            self.day = 1
            if self.month == 12:  # Nếu hết tháng 12 thì sang năm mới
                self.month = 1
                self.year += 1
            else:  # Chuyển sang tháng tiếp theo
                self.month += 1

    def is_leap_year(self, year):
        """Kiểm tra xem năm có phải là năm nhuận không."""
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Ví dụ sử dụng lớp Date:
if __name__ == "__main__":
    date = Date(28, 2, 2020)  # Ngày 28/02/2020 (năm nhuận)
    date.display()  # In ra ngày hiện tại
    date.next()     # Chuyển sang ngày tiếp theo
    date.display()  # In ra ngày tiếp theo