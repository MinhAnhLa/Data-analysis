import numpy as np
import pandas as pd
import seaborn as sns
import datetime as dt
import matplotlib.pyplot as plt


# Đọc dữ liệu từ tệp CSV
data = pd.read_csv("Online_Retail.csv", encoding="latin-1")

print("# Hiển thị 5 dòng đầu tiên của dữ liệu")
print(data.head())

print("# Thông tin tổng quan về dữ liệu")
print(data.info())

print("# Kiểm tra kiểu dữ liệu của từng cột")
print(data.dtypes)

print("# Thay đổi và kiểm tra kiểu dữ liệu:")
data = data.astype({'CustomerID': 'string',
                'InvoiceNo':'string'})
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
print(data.dtypes)


print("# Kiểm tra giá trị thiếu")
print(data.isnull().sum())

print("# Xử lý giá trị thiếu (loại bỏ các dòng có giá trị thiếu)")
data = data.dropna()
print(data.isnull().sum())


print("# Xem xét và xử lý các giá trị ngoại lệ")
print("# (ví dụ: loại bỏ các dòng có giá trị âm trong cột số lượng)")
data = data[data['Quantity'] > 0]
print(data)


print("# Tính tổng giá trị cho mỗi hóa đơn")
data['TotalValue'] = data['Quantity'] * data['UnitPrice']
print(data.head)
data = data.drop(data[data["TotalValue"]<=0].index)
print(data[data["TotalValue"]<=0].index)

sns.boxplot(data["TotalValue"])
Q1 = data["TotalValue"].quantile(0.25)
Q3 = data["TotalValue"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR
data = data[~((data["TotalValue"]>upper_limit) | (data["TotalValue"]<lower_limit))]
data.shape

sns.boxplot(data["TotalValue"])

