import pandas as pd

#1时间类型 时间差
aq = pd.read_csv('pandas/data/air_quality_no2_long.csv')

print(aq.to_csv('E:\OB\projects\DEMO\Knowledge\博一\量化交易\python-for-quant\看看no2long.csv'))
aq = aq.rename(columns={"date.utc": "datetime"})
print(aq["datetime"].dtype)                           # ① 现在是什么
aq["datetime"] = pd.to_datetime(aq["datetime"])       # ② 变成时间

print(aq["datetime"].dtype)                           # ③ 现在是什么
print(aq["datetime"].max() - aq["datetime"].min())    # ④ 两个时间相减

aq["month"]   = aq["datetime"].dt.month
print('这是月份',aq["month"].head(5))
aq["hour"]    = aq["datetime"].dt.hour
print('这是小时',aq["hour"].head(5))
aq["weekday"] = aq["datetime"].dt.weekday
print('这是周',aq["weekday"].head(5))
print(aq[["datetime", "month", "hour", "weekday"]].head().to_string())

by_day = aq.groupby([aq["datetime"].dt.weekday, "location"])["value"].mean()
print(by_day.to_string())

counts = aq.groupby([aq["datetime"].dt.weekday, "location"])["value"].size()
print(counts.unstack().to_string())




no2 = aq.pivot(index="datetime", columns="location", values="value")

print(no2.shape)
print(no2.head().to_string())
print(no2.isna().sum().to_string())


print(type(no2.index))
print(no2.index.year[:5])
print(no2.index.weekday[:5])




sub = no2["2019-05-20":"2019-05-21"]
print(sub.shape)
print(sub.index[0], "→", sub.index[-1])


monthly = no2.resample("ME").max()
print(monthly.to_string())
print("index.freq =", monthly.index.freq)



for alias in ["ME", "MS", "W", "D", "h"]:
    r = no2.resample(alias).mean()
    print(alias, "->", r.shape[0], "行   第一行标签:", r.index[0])



roll = no2.rolling(24).mean()
print(roll.shape)
print(roll.head(25).to_string())


r1 = no2.rolling(24).mean()
r2 = no2.rolling(24, min_periods=1).mean()
print(r1.notna().sum().to_string())
print(r2.notna().sum().to_string())
