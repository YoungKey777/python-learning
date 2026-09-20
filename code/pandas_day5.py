import pandas as pd

# no2 = pd.read_csv('pandas/data/air_quality_no2.csv')
# no2_long = pd.read_csv('pandas/data/air_quality_no2_long.csv')

# print(no2.shape)
# print(no2_long.shape)
# print(no2.head(3))
# print(no2_long.head(3))

# no2_melted = no2.melt(
#     id_vars=['datetime'],                                            # 哪一列「站着不动」
#     value_vars=['station_antwerp','station_paris','station_london'],  # 哪几列要被「摊平」
#     var_name='station',                                               # 摊平后：原来的【列名】放这
#     value_name='no2'                                                  # 摊平后：原来的【值】放这
# )

# print(no2_melted.shape)
# print(no2_melted.head())


# no2_back = no2_melted.pivot(
#     index='datetime',      # 拿哪一列当【新门牌】
#     columns='station',     # 拿哪一列的值当【新列名】
#     values='no2'           # 格子里的数字从哪来
# )

# print(no2_back.shape)
# print(no2_back.head(3))



aq = pd.read_csv('pandas/data/air_quality_long.csv')
print(aq.shape)
print(aq["parameter"].value_counts())

print(aq.pivot_table(
    index="location",       # 门牌放什么
    columns="parameter",    # 列放什么
    values="value",         # 格子里的数从哪来
    aggfunc="mean"          # ← 重复的格子里，怎么办
))