import pandas as pd
df = pd.read_csv('pandas/data/titanic.csv')
print(df.shape)
# print(df.head())

# df2 = df.set_index('Name')
# print(df2.head(3))
# print(df.head(3))



# Move Terminal into Editor Area

# df.info()  
# print(df.describe())   


df.to_csv('code/titanic_copy.csv', index=False)
df3 = pd.read_csv('code/titanic_copy.csv')
print(df3.shape)