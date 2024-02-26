import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Đọc dữ liệu từ tệp CSV
df = pd.read_csv("Online_Retail.csv", encoding="latin-1")

# Lọc và chọn các cột cần thiết (ví dụ: Quantity và UnitPrice)
selected_columns = ['Quantity', 'UnitPrice']
data = df[selected_columns]

# Loại bỏ các giá trị trống (NaN) và kiểm tra
data = data.dropna()
print(data.head())

# Chuẩn hóa dữ liệu
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Sử dụng K-means để phân cụm dữ liệu thành 4 cụm (có thể điều chỉnh theo nhu cầu của bạn)
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(scaled_data)

# Thêm cột 'Cluster' vào DataFrame
df['Cluster'] = kmeans.labels_

# Tạo biểu đồ đường cho từng cụm
plt.figure(figsize=(12, 6))
for cluster_label in range(4):  # Số lượng cụm
    cluster_data = df[df['Cluster'] == cluster_label]
    plt.plot(cluster_data.index, cluster_data['Quantity'], label=f'Cluster {cluster_label}')

plt.xlabel('Index')
plt.ylabel('Quantity')
plt.title('Biểu đồ đường theo từng cụm')
plt.legend()
plt.show()
