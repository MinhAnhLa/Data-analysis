import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ tệp CSV
df = pd.read_csv("Online_Retail.csv", encoding="latin-1")

# Sử dụng hàm `groupby()` để nhóm dữ liệu theo loại sản phẩm
grouped_df = df.groupby('Description')

# Sử dụng hàm `size()` để đếm số lượng sản phẩm trong mỗi nhóm
product_count = grouped_df.size()

# Chọn top 10 sản phẩm có số lượng ít nhất để vẽ biểu đồ
bottom_products = product_count.nsmallest(10)

# In ra số lượng của các sản phẩm
print("Số lượng của các sản phẩm:")
print(bottom_products)

# Tạo biểu đồ hình ảnh màu sắc
plt.bar(bottom_products.index, bottom_products.values, color="green")
plt.xticks(rotation=45, ha='right')  # Xoay tên sản phẩm để dễ đọc
plt.xlabel('Loại sản phẩm')
plt.ylabel('Số lượng')
plt.title('Top 10 Loại sản phẩm theo Số lượng')
plt.show()
