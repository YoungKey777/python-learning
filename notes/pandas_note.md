# **pandas** 学习笔记

> 记录方法：跟官方入门教程，每篇学完**关掉网页**，用自己的话写、在自己的数据上重敲一遍
> 来源：pandas 官方 Getting started tutorials（**2.3 版文档**，与本地版本一致）
> - 入口：https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/intro_tutorials/
> - 环境：Python 3.10.9 + pandas 2.3.3。pandas 3.0 要求 Python ≥3.11，本机装不了，所以**只看 2.3 版文档**（默认打开的 "latest" 是 3.0，行为不一样）

---

## 🧭 路线（8 天，每天一篇，约 40~60 分钟）

| 天 | 教程 | 当天练习 | 状态 |
|---|---|---|---|
| 0 | 数据落本地 | titanic 等抓进 `pandas/data/` | ✅ 5 个文件已落盘 |
| 1 | [01 数据结构](https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/intro_tutorials/01_table_oriented.html) + [02 读写](https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/intro_tutorials/02_read_write.html) | 读 titanic → `head/info/describe` → 写回 csv | 🟡 `read_csv`/`shape`/`head`/`set_index` 已跑通；`info`/`describe`/`to_csv` 待做 |
| 2 | [03 选取筛选](https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/intro_tutorials/03_subset_data.html) | `loc`/`iloc`/布尔索引：筛出"女性且票价 > 30" | ⬜ |
| 3 | [05 派生新列](https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/intro_tutorials/05_add_columns.html) | 向量化算 family_size、票价分箱（戒 for 循环） | ⬜ |
| 4 | [06 汇总统计](https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/intro_tutorials/06_calculate_statistics.html) | `groupby`：按舱位 × 性别算生存率 | ⬜ |
| 5 | [07 表变形](https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/intro_tutorials/07_reshape_table_layout.html) | `pivot`/`melt` 宽长互转 | ⬜ |
| 6 | [08 合并表](https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/intro_tutorials/08_combine_dataframes.html) | `concat`/`merge` 把两张表拼起来 | ⬜ |
| 7 | [09 时间序列](https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/intro_tutorials/09_timeseries.html) ★ | `resample` 日→月 + `rolling` 20 日均线 | ⬜ |
| 8 | 收口 | 完整走一遍"读 CSV → 统计 → 出结论"，脚本存 `code/` | ⬜ |

- **挂账**：[04 画图](https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/intro_tutorials/04_plotting.html) 并进阶段 3 可视化一起学；[10 文本数据](https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/intro_tutorials/10_text_data.html) 选学
- **验收（第 8 天自测）**：不看文档写出 `groupby` / `merge` / `resample` / `rolling`，并说清 `loc` 和 `iloc` 的区别——对上了 roadmap 阶段 2 的检验标准"读 CSV → 算收益率 → 画图"

### 每天固定动作

1. 读当天那篇（十几分钟）
2. **关掉网页**，在自己的数据上把 3 个关键操作重写一遍，不许复制粘贴
3. 在下面填当天小节 → 存 `code/` 脚本 → `push.bat` 打卡

## ⚠️ 网络备忘：教程里的数据从 github 拉不通

教程代码里的 `https://github.com/pandas-dev/pandas/raw/main/doc/data/xxx.csv` 在本机直连失败（实测连接被拒），换成 jsDelivr 镜像即可：

```
https://cdn.jsdelivr.net/gh/pandas-dev/pandas@main/doc/data/xxx.csv
```

替换规则：`github.com/pandas-dev/pandas/raw/main/` → `cdn.jsdelivr.net/gh/pandas-dev/pandas@main/`（实测可访问）

**✅ 已落盘（2026-09-14）**，换台机器就重跑这一条：

```bash
mkdir -p pandas/data && cd pandas/data
B="https://cdn.jsdelivr.net/gh/pandas-dev/pandas@main/doc/data"
for f in titanic.csv air_quality_no2.csv air_quality_no2_long.csv air_quality_long.csv air_quality_parameters.csv; do
  curl -L --retry 3 -O "$B/$f"
done
```

（`air_quality_no2.csv` 第一次可能超时，`--retry 3` 会自己重试——不是地址错）

| 文件 | 形状 | 大小 |
|---|---|---|
| `titanic.csv` | (891, 12) | 59 KB |
| `air_quality_no2.csv` | (1035, 4) | 31 KB |
| `air_quality_no2_long.csv` | (2068, 7) | 133 KB |
| `air_quality_long.csv` | (5272, 7) | 349 KB |
| `air_quality_parameters.csv` | (7, 3) | 255 B |

> 形状是**实跑 `df.shape` 出来的**，不是抄的——Day 1 跑完对不上就说明读错了文件。

---

## Day 1 · 数据结构 & 读写

> **一句话**：pandas 的核心是一张表（**DataFrame**）——**一行一条记录，一列一项信息**，外加一列 pandas 自己发的「名牌」叫 **index**。
>
> 🔗 对照：你在 ArcGIS 里打开 shapefile 看到的**属性表**，就是同一个东西。一行 = 一个要素，一列 = 一个字段。

### 关键操作 ① `pd.read_csv()` —— 把 CSV 变成表

```python
import pandas as pd                          # 请 pandas 进来，起外号 pd（打字短）

df = pd.read_csv('pandas/data/titanic.csv')  # 读进来，装进名叫 df 的盒子
```

- `df` 是变量名，取 **D**ata**F**rame 的前两个字母；叫 `data`、`titanic` 也完全可以，纯属习惯
- 装进去的东西，类型就叫 `DataFrame` —— 一张表

### 关键操作 ② `df.shape` —— 问它「你多大」

```python
print(df.shape)      # → (891, 12)
```

- **顺序永远是 `(行数, 列数)`** —— 行在前，列在后，pandas 里没有例外

> ⚠️ **语法上的关键区别：`df.shape` 不加括号，`df.head()` 要加括号**
>
> - **不加括号 = 属性**（property）—— 直接取得的一个东西，像 `.real`、`.imag` 那样
> - **加括号 = 方法**（method）—— 执行一个**动作**
>
> 记法：`shape` 是「你多高」——静态的；`head()` 是「把头 5 行拿来」——一个动作。

### 关键操作 ③ `df.head()` / `df.set_index()` —— 看长相 / 换名牌

```python
print(df.head())                 # 前 5 行（默认 5；写 head(10) 就看 10 行）
print(df.head(3))                # 前 3 行

df2 = df.set_index('Name')       # 把 Name 这一列，改装成 index
print(df2.head(3))
```

- `head()` 输出的**最后一行** `[5 rows x 12 columns]` **不是数据**，是 pandas 在说「我只给你看了 5 行，完整的 891 行」
- `set_index('Name')` 之后，表尾变成 `[3 rows x 11 columns]` —— **列数从 12 掉到 11**
  - **少的就是 `Name`**：它从「数据列」搬出去当「名牌」了
  - 这是最硬的证据：**index 不占数据列的位置 —— 它不是数据，是名牌**

### index（索引）到底是什么

表最左边那列 `0 1 2 3 4...`，你没要求显示，它自己就在。

**它不是装饰，是抓手。** 是每行挂的一块名牌，pandas 靠它定位和对齐。

两个精准的类比：

| 类比 | 对应关系 |
|---|---|
| **ArcGIS 属性表里的 FID** | 一模一样：自动生成、每行一个、不重复 |
| **列表 / 数组的下标** | 默认就是 `0,1,2...`，从 0 数起 |

但名牌**可以换** —— `set_index('Name')` 一换，左边就成人名了。

> 📌 `[5 rows x 12 columns]` 这种**方括号包的尾巴**，以后会一直出现。记住它不属于数据，是 pandas 的「旁白」。

### 踩的坑

**① 相对路径认的是「你站在哪」，不是「脚本在哪」** —— 这个坑连着踩了 3 次

```powershell
PS E:\OB\projects\DEMO\Knowledge>     # ← 提示符里这串 = 你现在站的地方
```

| 脚本在哪 | 你站在哪 | 路径该写什么 |
|---|---|---|
| `python-for-quant\code\` | `python-for-quant\` | `pandas/data/titanic.csv` |
| `python-for-quant\code\` | `code\` | `..\pandas\data\titanic.csv` |

**两边必须配对。** 对不上就是 `FileNotFoundError`。

**② `.\` 和 `..\` 也是相对路径** —— 相对的那个「谁」，**还是你站的地方**

实测同一行代码，只换站位：

| 你站在 | `pandas/data/titanic.csv` | `./pandas/data/titanic.csv` | `../pandas/data/titanic.csv` |
|---|---|---|---|
| `Knowledge\` | ❌ | ❌ | ❌ |
| `python-for-quant\` | ✅ | ✅ | ❌ |
| `python-for-quant\code\` | ❌ | — | ✅ |

- `.\pandas\...` 跟不写 `.\` **完全一样**（`.` 就是「这儿」，写了等于没写）
- `..\pandas\...` = 先往上走一层，再往下找
- 关键结论：**`..\` 只在「你站的地方」和「文件在哪」差固定层数时才对得上**，不是万能钥匙

**③ 报错时第一反应不是改代码，是看提示符** —— 报错说「找不到文件」，先看 `PS ...` 那串

## Day 2 · 选取筛选（loc / iloc / 布尔）

> 待填：一句话 / 3 个关键操作 / 踩的坑

## Day 3 · 派生新列（向量化）

> 待填：一句话 / 3 个关键操作 / 踩的坑

## Day 4 · 汇总统计（groupby）

> 待填：一句话 / 3 个关键操作 / 踩的坑

## Day 5 · 表变形（pivot / melt）

> 待填：一句话 / 3 个关键操作 / 踩的坑

## Day 6 · 合并表（concat / merge）

> 待填：一句话 / 3 个关键操作 / 踩的坑

## Day 7 · 时间序列（DatetimeIndex / resample / rolling）★

> 待填：一句话 / 3 个关键操作 / 踩的坑

## Day 8 · 收口实战

> 待填：做了什么 / 结论 / 还欠什么

---

## 🔧 环境与坑（随时追加）

- **pandas 版本**：本机 2.3.3（`python -c "import pandas; print(pandas.__version__)"` 可查）；3.0 需 Python ≥3.11，暂不升
- **数据不落盘就别谈分析**：教程里的数据先存 `pandas/data/`，练习全部读本地文件（省得每次联网 + 结果可复现）

---
*所属模块：[[python-for-quant/roadmap|roadmap]] 阶段 2（numpy + pandas）；相关笔记 [[notes/python_note|python_note]]*
