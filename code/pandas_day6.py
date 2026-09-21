import pandas as pd

aq = pd.read_csv('pandas/data/air_quality_long.csv')

# no2  = aq[aq["parameter"] == "no2"]      # 只留 no2 的行（Day 2 的筛行）
# pm25 = aq[aq["parameter"] == "pm25"]     # 只留 pm25 的行

# print(no2.shape)
# print(no2.head())
# print(pm25.shape)
# print(pm25.head())

# aq_back = pd.concat([pm25,no2])         # 摞回去
# print(aq_back.shape)
# print(aq_back.head())
# print(aq.head())

params = pd.read_csv('pandas/data/air_quality_parameters.csv')
print(params.shape)
print(params.head())

merged = aq.merge(
    params,
    left_on="parameter",     # 左边这张表，用哪一列去配
    right_on="id"            # 右边那张表，用哪一列来对
)
# print(merged.shape)
# print(merged.head(3))

params_cut = params[params["id"] != "pm25"]

lost = aq.merge(params_cut, left_on="parameter", right_on="id")
print(lost.shape)
print(lost.head())

kept = aq.merge(params_cut, left_on="parameter", right_on="id", how="left")
print("kept:", kept.shape)
print(kept[kept["parameter"] == "pm25"].head(3))

for how in ["inner", "left", "right", "outer"]:
    r = aq.merge(params_cut, left_on="parameter", right_on="id", how=how)
    print(f"{how:6} {r.shape}")

right = aq.merge(params_cut, left_on="parameter", right_on="id", how="right")
print(right[right["city"].isna()])


# 重新读一份，别动刚才的 aq
aq2 = pd.read_csv('pandas/data/air_quality_long.csv')

# 把 parameter 这一列的每个值都变成大写（.str 是「按字符串处理」）
aq2["parameter"] = aq2["parameter"].str.upper()

bad = aq2.merge(params, left_on="parameter", right_on="id", how="left")
print("bad:", bad.shape)
print(bad[["id", "description", "name"]].notna().sum())

print(pd.concat([aq[["parameter", "value"]].head(3),
                 params[["id", "name"]].head(3)], axis=1))