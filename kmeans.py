import numpy as np
import pandas as pd
import seaborn as sns
import datetime as dt
import matplotlib.pyplot as plt

# Đọc dữ liệu từ tệp CSV
df = pd.read_csv("Online_Retail.csv", encoding="latin-1")

df = df.dropna()
print(df.isnull().sum())

print("# Tính tổng giá trị cho mỗi hóa đơn")
df['Total'] = df['Quantity'] * df['UnitPrice']
print(df.head)
df = df.drop(df[df["Total"]<=0].index)
print(df[df["Total"]<=0].index)

df = df.reset_index(drop=True)
df

df["CustomerID"].nunique()

df["InvoiceNo"].nunique()

df["CustomerID"] = df["CustomerID"].astype("int")
df.info()

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df.info()

lastday = df["InvoiceDate"].max()
lastday

r = (lastday - df.groupby("CustomerID").agg({"InvoiceDate":"max"})).apply(lambda x:x.dt.days)
f = df.groupby(["CustomerID","InvoiceNo"]).agg({"InvoiceNo":"count"})
f = f.groupby("CustomerID").agg({"InvoiceNo":"count"})
m = df.groupby("CustomerID").agg({"Total":"sum"})

RFM = r.merge(f, on="CustomerID").merge(m, on="CustomerID")
RFM = RFM.reset_index()
RFM = RFM.rename(columns={"InvoiceDate":"Recency", "InvoiceNo":"Frequency", "Total":"Monetary"})
RFM.head()

df = RFM.iloc[:,1:]
df.head()

from sklearn.preprocessing import MinMaxScaler
from yellowbrick.cluster import KElbowVisualizer
from sklearn.cluster import KMeans


sc = MinMaxScaler()
dfnorm = sc.fit_transform(df)
dfnorm = pd.DataFrame(dfnorm, columns=df.columns)
dfnorm


kmodel = KMeans(random_state = 0)
grafik = KElbowVisualizer(kmodel, k=(2,10))
grafik.fit(dfnorm)
grafik.poof()

kmodel = KMeans(n_init='auto', random_state=0)

kmodel = KMeans(random_state=0, n_clusters=4, init="k-means++")
kfit = kmodel.fit(dfnorm)
labels = kfit.labels_

sns.scatterplot(x = "Recency", y = "Frequency", data = dfnorm, hue = labels, palette="deep")
plt.show

RFM["Labels"] = labels
RFM

#RFM.groupby("Labels")["CustomerID"].count()
RFM.groupby("Labels").mean().iloc[:,1:]

RFM.set_index('CustomerID', inplace=True)
RFM.drop(columns=['Labels'], inplace=True)
RFM
RFM.describe().T
"""
RFM["RecencyScore"] = pd.qcut(RFM["Recency"], 5, labels = [5, 4 , 3, 2, 1])
RFM["FrequencyScore"]= pd.qcut(RFM["Frequency"].rank(method="first"),5, labels=[1,2,3,4,5])
RFM["MonetaryScore"] = pd.qcut(RFM['Monetary'], 5, labels = [1, 2, 3, 4, 5])

"""
RFM["RecencyScore"] = pd.qcut(RFM["Recency"], 3, labels=[3, 2, 1])
RFM["FrequencyScore"] = pd.qcut(RFM["Frequency"].rank(method="first"), 3, labels=[1, 2, 3])
RFM["MonetaryScore"] = pd.qcut(RFM['Monetary'], 3, labels=[1, 2, 3])
RFM["RFM_SCORE"] = (RFM["RecencyScore"].astype(str) + RFM["FrequencyScore"].astype(str))
RFM.head()

"""
seg_map = {
    r'[1-2][1-2]': 'hibernating',22
    r'[1-2][3-4]': 'at_Risk',12
    r'[1-2]5': 'cant_loose',13
    r'3[1-2]': 'about_to_sleep',2[1]
    r'33': 'need_attention',22
    r'[3-4][4-5]': 'loyal_customers',[2]3
    r'41': 'promising',31
    r'51': 'new_customers',31
    r'[4-5][2-3]': 'potential_loyalists', [3][2]
    r'5[4-5]': 'champions' 3[3]
}
RFM['segment'] = RFM['RFM_SCORE'].replace(seg_map, regex=True)
RFM.head()
"""
seg_map = {
    r'[1][1]': 'So bad',
    r'[2][2]': 'hibernating',
    r'[1][2]': 'at_Risk',
    r'[1]3': 'cant_loose',
    r'2[1]': 'about_to_sleep',
    r'22': 'need_attention',
    r'[2][3]': 'loyal_customers',
    #r'31': 'promising',31
    r'31': 'new_customers',
    r'[3][2]': 'potential_loyalists',
    r'33': 'champions'
}
RFM['segment'] = RFM['RFM_SCORE'].replace(seg_map, regex=True)
RFM.head()

RFM[["segment", "Recency","Frequency","Monetary"]].groupby("segment").agg(["mean","count","max"]).round()

import squarify

segments = RFM["segment"].value_counts().sort_values(ascending=False)
fig = plt.gcf()
ax = fig.add_subplot()
fig.set_size_inches(16, 10)

# Make sure that you have enough labels for each segment
labels = [label for label in seg_map.values()][:len(segments)]

squarify.plot(
    sizes=segments,
    label=labels,
    color=[
        "#AFB6B5",
        "#F0819A",
        "#926717",
        "#F0F081",
        "#81D5F0",
        "#C78BE5",
        "#748E80",
        "#FAAF3A",
        "#7B8FE4",
        "#86E8C0",
    ],
    pad=False,
    bar_kwargs={"alpha": 1},
    text_kwargs={"fontsize": 15},
)
plt.title("Bản đồ phân khúc khách hàng", fontsize=20)
plt.xlabel("Frequency", fontsize=18)
plt.ylabel("Recency", fontsize=18)
plt.show()