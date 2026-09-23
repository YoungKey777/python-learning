import numpy as np
import pandas as pd

nums = [1.2, 3.4, 5.6]      # 你早就有的东西：一个 list
a    = np.array(nums)       # 同一个东西的 numpy 版本

print("list  * 2 ->", nums * 2)
print("array * 2 ->", a * 2)

print(a.shape)
print(a.dtype)
print(a.ndim)

df = pd.read_csv('pandas/data/titanic.csv')

s = df["Age"].to_numpy()      # ← 脱壳：Series 变成 ndarray

print(df.shape)               # 表的 shape
print(df.head())
print(s.shape, s.dtype)       # 壳底下那根数组的 shape 和 dtype


arr = df.to_numpy()

print(arr.shape, arr.dtype)
