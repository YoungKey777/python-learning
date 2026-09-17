import pandas as pd

df = pd.read_csv('pandas/data/titanic.csv')

# ==================== 热身：补昨天欠的切片规则 ====================
# print(df.loc[0:2, "Age"])      # 标签切片 → 两头都算   → 3 个数
# print(df.iloc[0:2, 5])         # 位置切片 → 不含右边   → 2 个数

# ==================== Day 3 · 一、向量化：一列当整体算 ====================
# 家庭人数 = 兄弟姐妹数(SibSp) + 父母子女数(Parch) + 自己
# fs = df["SibSp"] + df["Parch"] + 1
# print(fs.shape)                # (891,)  ← 891 个一次算完，一行 for 都没写
# print(fs.head())

fs = df["SibSp"] + df["Parch"] + 1
# print(fs.shape)
# print(fs.head())

# print(df["SibSp"].head())                    # ①
# print(df["Parch"].head())                    # ②
# print((df["SibSp"] + df["Parch"]).head())    # ③

# df["family_size"] = fs

# print(df.shape)                   # 猜猜
# print(df["family_size"].head())




# df["is_child"] = df["Age"] < 18
# # print(df["is_child"].head())
# # print(df["is_child"].dtype)
# print(df["is_child"].sum())
# print(df[df["Age"] < 18].shape)

df["fare_level"] = pd.cut(
    df["Fare"],                            # 切哪一列
    bins=[0, 10, 30, 100, 600],            # 5 个切点 → 切出 4 段
    labels=["便宜", "中", "贵", "土豪"]       # 4 段，4 个名字
)

print(df["fare_level"].head())
print(df["fare_level"].value_counts(dropna=False))