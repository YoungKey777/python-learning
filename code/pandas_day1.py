import pandas as pd
df = pd.read_csv('pandas/data/titanic.csv')
print(df.shape)
print(df.head())

df2 = df.set_index('Name')
print(df2.head(3))