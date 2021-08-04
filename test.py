# 欠損値がある列はどの列か
# 損値については「9999999」で埋めて下さい
# 年齢を60歳以上に絞った行数は何件か

import pandas as pd

df = pd.read_csv(r'/Users/shunsasaki/Downloads/test.csv', header=1)

print(df.isnull().any(axis=0))
print(df.fillna(999999))
print(df[df['age'] > 60])
df["id"].fillna(999999)

for col in df.columns:
    if df[col].isnull().sum():
        print(col)
