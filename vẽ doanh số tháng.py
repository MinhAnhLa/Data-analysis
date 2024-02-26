import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ tệp CSV
df = pd.read_csv("Online_Retail.csv", encoding="latin-1")

# Chuyển cột InvoiceDate sang định dạng datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Sử dụng hàm `groupby()` để nhóm dữ liệu theo tháng
grouped_df = df.groupby(df['InvoiceDate'].dt.to_period("M"))

# Sử dụng hàm `size()` để đếm số lượng đơn hàng trong mỗi nhóm
total_order_count = grouped_df.size()

# Tạo một Series chứa số lượng đơn hàng theo tháng
order_count_by_month = total_order_count.to_frame()

# Đặt tên cột
order_count_by_month.columns = ["Số lượng đơn hàng"]
# In ra doanh số tháng
print("Doanh số tháng:")
print(order_count_by_month)

# Định dạng lại cột x để hiển thị tháng/năm
plt.xticks(rotation=45, ha="right")
plt.xlabel('Tháng/Năm')


# Tạo biểu đồ hình ảnh màu sắc
plt.bar(order_count_by_month.index.astype(str), order_count_by_month["Số lượng đơn hàng"], color="blue")
plt.show()

