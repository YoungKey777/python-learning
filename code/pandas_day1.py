# cd "E:\OB\projects\DEMO\Knowledge\博一\量化交易\python-for-quant"
# import pandas as pd
# df = pd.read_csv('pandas/data/titanic.csv')
# print(df.shape)
# print(df.head())

# df2 = df.set_index('Name')
# print(df2.head(3))
# print(df.head(3))


# Move Terminal into Editor Area

# df.info()  
# print(df.describe())   


# df.to_csv('code/titanic_copy.csv', index=False)
# df3 = pd.read_csv('code/titanic_copy.csv')
# print(df3.shape)


# import pandas as pd
#df = pd.read_csv('pandas/data/titanic.csv')

# a = df["Age"]
# print(a.shape)

# b = df[["Age", "Sex"]]
# print(b.shape)


# c = df[["Age"]]
# print(c.shape)




# mask = df["Age"] > 35
# print(mask.shape)
# print(mask.head())

# above35 = df[mask]
# print(above35.shape)

# print(above35.head())


# mask2 = df["Age"].notna()
# print(mask2.shape)
# print(mask2.head())

# df_no_hole = df[mask2]
# print(df_no_hole.shape)






import pandas as pd

df = pd.read_csv('pandas/data/titanic.csv')

# ==================== 一、选列 ====================
# a = df["Age"]              # 单括号 → 抽走一条线 → Series
# print(a.shape)             # (891,)   1 个数 = 一维，只有长度

# b = df[["Age", "Sex"]]     # 双括号 → 切下一块表 → DataFrame
# print(b.shape)             # (891, 2) 2 个数 = 二维

# c = df[["Age"]]            # 双括号只取一列 → 还是表，只是窄
# print(c.shape)             # (891, 1) ← 括号层数才是决定因素

# # ==================== 二、筛行 ====================
mask = df["Age"] > 35      # ① 造名单：891 个 True/False
# print(mask.shape)          # (891,)   ← 和原表一样长，一行一个答案
# print(mask.head())         # dtype: bool

above35 = df[mask]         # ② 执行名单：True 的行留下，整行都留
# print(above35.shape)       # (217, 12) ← 行少了，列一根没少
# print(above35.head())      # 门牌号跳号：1, 6, 11, 13, 15

# mask2 = df["Age"].notna()  # 换个问法："这格不是洞吗？"
# print(mask2.shape)         # (891,)
# df_no_hole = df[mask2]     # 执行名单
# print(df_no_hole.shape)    # (714, 12) ← 就是 info() 里那个 714

# ==================== 三、loc / iloc ====================
# print(df.iloc[0].shape)    # 取一行 → (12,) ← 这个 12 是从"列"来的
# # print(df.iloc[0].head(13)) 
# print(df.loc[0, "Age"])    # 用名字找 → 22.0
# print(df.iloc[0, 5])       # 用位置找 → 22.0  （Age 是第 5 列）

# print(above35.iloc[0, 5])     # 位置 0
# print(above35.loc[1, "Age"])  # 门牌号 1
# print(above35.loc[0, "Age"])  # 门牌号 0 ← 这行会报错

mask3 = (df["Sex"] == "female") & (df["Fare"] > 30)
# print(mask3.shape)
# print(df[mask3].shape)

print(df["Sex"].value_counts())