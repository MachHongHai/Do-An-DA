import pandas as pd

df = pd.read_csv("data/airline.csv")

print("Kích thước dữ liệu:", df.shape)

print(df.head())

print("Danh sách cột:")
for col in df.columns:
    print("-", col)

print("Thông tin dữ liệu:")
df.info()
df.describe()