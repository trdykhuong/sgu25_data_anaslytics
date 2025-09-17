import math

# Nhập bán kính từ người dùng (kiểu float)
r = float(input("Nhập bán kính hình tròn: "))

# Tính chu vi và diện tích
cv = 2 * math.pi * r
dt = math.pi * r ** 2

# Xuất kết quả
print(f"Chu vi hình tròn: {cv:.2f}")
print(f"Diện tích hình tròn: {dt:.2f}")
