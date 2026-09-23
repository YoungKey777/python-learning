import akshare as ak
import pandas as pd

df = ak.stock_zh_index_daily(symbol="sh000001")       # ① 拉
df.to_csv('pandas/data/sh000001.csv', index=False)    # ② 落盘

d = pd.read_csv('pandas/data/sh000001.csv')           # ③ 读本地
print(d.shape)
print(d.head(3).to_string())
print("date 列的 dtype:", d["date"].dtype)