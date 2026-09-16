import pandas as pd

df = pd.read_csv('pandas/data/titanic.csv')

# ==================== 一、选列 ====================
a = df["Age"]              # 单括号 → 抽走一条线 → Series（一维）
print(a.shape)             # (891,)   1 个数 = 一维，只有长度

b = df[["Age", "Sex"]]     # 双括号 → 切下一块表 → DataFrame（二维）
print(b.shape)             # (891, 2)

c = df[["Age"]]            # 双括号只取一列 → 还是表，只是窄
print(c.shape)             # (891, 1) ← 括号层数才是决定因素，不是取了几列

# 取一行 = 一张竖过来的表（列名跑到左边当标签）；891 来自行数，12 来自列数
print(df.iloc[0].shape)    # (12,)

# ==================== 二、筛行 ====================
mask = df["Age"] > 35      # ① 造名单：891 个 True/False
print(mask.shape)          # (891,) ← 和原表一样长，一行一个答案
print(mask.head())         # dtype: bool

above35 = df[mask]         # ② 执行名单：True 的行留下，整行都留
print(above35.shape)       # (217, 12) ← 行少了，列一根没少
print(above35.head())      # 门牌号跳号：1, 6, 11, 13, 15

mask2 = df["Age"].notna()  # 换个问法："这格不是洞吗？"（反面 isna()）
print(mask2.shape)         # (891,)
df_no_hole = df[mask2]     # 执行名单
print(df_no_hole.shape)    # (714, 12) ← 就是 info() 里那个 714

# 多个条件：用 & 不是 and，且每个条件自己裹一层括号（& 优先级比 > 高）
mask3 = (df["Sex"] == "female") & (df["Fare"] > 30)
print(mask3.shape)         # (891,)
print(df[mask3].shape)     # (113, 12)

# ==================== 三、loc / iloc ====================
print(df.loc[0, "Age"])    # 用名字找 → 22.0
print(df.iloc[0, 5])       # 用位置找 → 22.0（Age 是第 5 列）

# 筛完之后门牌和位置分家：
print(above35.iloc[0, 5])     # 第 0 个   → 38.0
print(above35.loc[1, "Age"])  # 门牌 1 号 → 38.0  ← 同一行
# print(above35.loc[0, "Age"])  # 门牌 0 号 → KeyError: 0（故意留这行做记号：0 号被筛掉了）

# ==================== 四、还 Day 1 的债：文字列怎么统计 ====================
print(df["Sex"].value_counts())   # male 577 / female 314，加起来 891
