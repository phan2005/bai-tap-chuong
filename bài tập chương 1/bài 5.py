class Stack:
    def __init__(self, capacity):
        # Khởi tạo ngăn xếp với kích thước được chỉ định
        self.capacity = capacity  
        self.stack = []           
        self.top = -1             

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity - 1

    def push(self, value):
        if self.isFull():
            print("Ngăn xếp đã đầy. Không thể thêm phần tử.")
        else:
            self.top += 1
            self.stack.append(float(value))  # Đảm bảo phần tử được thêm là kiểu float
            print(f"Đã thêm {value} vào ngăn xếp.")

    def pop(self):
        if self.isEmpty():
            print("Ngăn xếp rỗng. Không thể lấy phần tử.")
            return None
        else:
            popped_value = self.stack.pop()
            self.top -= 1
            print(f"Đã lấy {popped_value} ra khỏi ngăn xếp.")
            return popped_value

    def count(self):
        return self.top + 1

    def display(self):
        if self.isEmpty():
            print("Ngăn xếp rỗng.")
        else:
            print("Ngăn xếp hiện tại:", self.stack)


# Sử dụng lớp Stack
stack = Stack(capacity=5)  # Tạo ngăn xếp với sức chứa tối đa là 5

stack.push(1.2)
stack.push(2.3)
stack.push(3.4)

stack.display()

print(f"Số phần tử hiện có trên ngăn xếp: {stack.count()}")  # In ra số lượng phần tử hiện tại

stack.pop()
stack.display()

print(f"Số phần tử hiện có trên ngăn xếp: {stack.count()}")