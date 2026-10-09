import pandas as pd

#1. Đọc hai file gốc từ Kaggle
train = pd.read_csv("data/raw/train.csv")
test = pd.read_csv("data/raw/test.csv")

#2. Kiểm tra kích thước (số dòng, số cột) của từng file
print("Kích thước file train:", train.shape)
print("Kích thước file test:", test.shape)

#3. Kiểm tra hai file có cùng cột trước khi gộp, nếu lệch cột thì concat sẽ sinh NaN ở các cột không khớp
print("Hai file có cùng cột:",
      train.columns.tolist() == test.columns.tolist())

#4. Nối hai file theo chiều dòng, đánh lại index từ 0
df = pd.concat([train, test], ignore_index=True)
print("Kích thước sau khi gộp:", df.shape)

df.to_csv("data/airline.csv", index=False)
print("Đã lưu data/airline.csv")
