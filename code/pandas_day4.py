import pandas as pd
df = pd.read_csv('pandas/data/titanic.csv')

print(df["Age"].mean())                      # 不分：一个数
print(df.groupby("Sex")["Age"].mean())       # 按 Sex 分：？

print(df.groupby("Sex")["Age"].size())     # 每堆有多少人
print(df.groupby("Sex")["Age"].count())    # 每堆有多少个「有年龄记录」的

print(df.groupby("Sex")["Survived"].mean())              # 按性别
print(df.groupby(["Sex", "Pclass"])["Survived"].mean())  # 按性别 × 舱位