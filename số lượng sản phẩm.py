import pandas as pd

# Đọc dữ liệu từ tệp CSV
df = pd.read_csv("Online_Retail.csv", encoding="latin-1")

# Lấy danh sách duy nhất các sản phẩm
all_products = df['Description'].unique()

# In ra một số lượng nhất định (ví dụ: 20 sản phẩm)
sample_size = 20
sample_products = all_products[:sample_size]

# In ra mẫu sản phẩm
print(f"Mẫu {sample_size} sản phẩm:")
for product in sample_products:
    print(product)
