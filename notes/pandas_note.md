# **pandas** 学习笔记

> 记录方法：跟官方入门教程，每篇学完**关掉网页**，用自己的话写、在自己的数据上重敲一遍
> 来源：pandas 官方 Getting started tutorials（**2.3 版文档**，与本地版本一致）
> - 入口：https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/intro_tutorials/
> - 环境：Python 3.10.9 + pandas 2.3.3。pandas 3.0 要求 Python ≥3.11，本机装不了，所以**只看 2.3 版文档**（默认打开的 "latest" 是 3.0，行为不一样）

---

## 🧭 路线（8 天，每天一篇，约 40~60 分钟）

| 天   | 教程                                                                                                                                                                                                                                  | 当天练习                                      | 状态                                                                         |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- | -------------------------------------------------------------------------- |
| 0   | 数据落本地                                                                                                                                                                                                                               | titanic 等抓进 `pandas/data/`                | ✅ 5 个文件已落盘                                                                 |
| 1   | [01 数据结构](https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/intro_tutorials/01_table_oriented.html) + [02 读写](https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/intro_tutorials/02_read_write.html) | 读 titanic → `head/info/describe` → 写回 csv | ✅ 六个动作全跑通；写回后重读 `(891, 12)` 对得上 |
| 2   | [03 选取筛选](https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/intro_tutorials/03_subset_data.html)                                                                                                                    | `loc`/`iloc`/布尔索引：筛出"女性且票价 > 30"          | ⬜                                                                          |
| 3   | [05 派生新列](https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/intro_tutorials/05_add_columns.html)                                                                                                                    | 向量化算 family_size、票价分箱（戒 for 循环）           | ⬜                                                                          |
| 4   | [06 汇总统计](https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/intro_tutorials/06_calculate_statistics.html)                                                                                                           | `groupby`：按舱位 × 性别算生存率                    | ⬜                                                                          |
| 5   | [07 表变形](https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/intro_tutorials/07_reshape_table_layout.html)                                                                                                            | `pivot`/`melt` 宽长互转                       | ⬜                                                                          |
| 6   | [08 合并表](https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/intro_tutorials/08_combine_dataframes.html)                                                                                                              | `concat`/`merge` 把两张表拼起来                  | ⬜                                                                          |
| 7   | [09 时间序列](https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/intro_tutorials/09_timeseries.html) ★                                                                                                                   | `resample` 日→月 + `rolling` 20 日均线         | ⬜                                                                          |
| 8   | 收口                                                                                                                                                                                                                                  | 完整走一遍"读 CSV → 统计 → 出结论"，脚本存 `code/`       | ⬜                                                                          |

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

### 关键操作 ④ `df.info()` —— 看底细（哪列有洞）

```python
df.info()                        # 不用 print，它自己会往屏幕上打
```

输出（节选）：

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  891 non-null    int64  
 5   Age          714 non-null    float64
 10  Cabin        204 non-null    object 
 11  Embarked     889 non-null    object 
dtypes: float64(2), int64(5), object(5)
memory usage: 83.7+ KB
```

**`info()` 是「进门先做的全身检查」，一次给五样：**

| 告诉你什么 | 在输出里 |
|---|---|
| 什么类型 | `<class 'pandas.core.frame.DataFrame'>` ← `df` 是 `DataFrame` 类的**实例** |
| 多少行 | `891 entries, 0 to 890` |
| 每列的**类型** | `Dtype` 列 |
| 每列的**非空数** | `Non-Null Count` 列 |
| 占多大内存 | `memory usage` |

**重点是 `Non-Null Count` 那一列** —— 拿它跟总行数 891 一比，哪列有洞立刻现形：

| 列 | Non-Null | 891 − 它 = **洞** |
|---|---|---|
| `PassengerId` | 891 | 0 |
| `Age` | 714 | **177** |
| `Cabin` | 204 | **687** |
| `Embarked` | 889 | **2** |
| 其余 8 列 | 891 | 0 |

> 📌 **「真实数据是有洞的」第一次撞到脸上**：891 个乘客，177 个年龄不详、**687 个舱位不详（四分之三）**。
> 以后拿到**任何**一张表，第二个动作永远是 `df.info()`。这不是教程规矩，是保命习惯。

跟 `head()` 对比：`head()` 看**长相**（塞满你眼前 5 行，看着挺完整）；`info()` 看**底细**（891 行全貌，一眼看出哪列是筛子）。

> ⚠️ `info()` 不是「查空专用工具」，它只是**顺手**告诉你空值。专门查空的另有其人（`isnull()`），以后教。

### 关键操作 ⑤ `df.describe()` —— 看统计

```python
print(df.describe())             # 这个要套 print
```

```
       PassengerId    Survived      Pclass         Age  ...        Fare
count   891.000000  891.000000  891.000000  714.000000  ...  891.000000
mean    446.000000    0.383838    2.308642   29.699118  ...   32.204208
std     257.353842    0.486592    0.836071   14.526497  ...   49.693429
min       1.000000    0.000000    1.000000    0.420000  ...    0.000000
25%     223.500000    0.000000    2.000000   20.125000  ...    7.910400
50%     446.000000    0.000000    3.000000   28.000000  ...   14.454200
75%     668.500000    1.000000    3.000000   38.000000  ...   31.000000
max     891.000000    1.000000    3.000000   80.000000  ...  512.329200
```

两个要点：

1. **`count` 行 = `info()` 的 `Non-Null Count`** —— 同一个数（`Age` 都是 714）。算统计量前先数数有几个数，pandas 也是这习惯
2. **只统计了 7 列，不是 12 列** —— `describe()` 默认只算**数字列**

**为什么跳过文字列**：`describe()` 算的是 `mean`（平均）、`std`（标准差），你让 pandas 求 `"male"` 和 `"female"` 的平均值，它没法算。**文字没有平均值。**

> 文字列不是统计不了，是得换个问法 —— 不问「平均多少」，问「**各有多少个**」。Day 2 头一道题。

**`Dtype` 三档**（就是 `info()` 输出里那一列）：

| dtype | 意思 | titanic 里 |
|---|---|---|
| `int64` | 整数 | `PassengerId` `Survived` `Pclass` `SibSp` `Parch` |
| `float64` | 小数 | `Age` `Fare` |
| `object` | **文字**（字符串） | `Name` `Sex` `Ticket` `Cabin` `Embarked` |

`int64`(5) + `float64`(2) = **7** —— 正好是 `describe()` 输出的那 7 列。

### 关键操作 ⑥ `df.to_csv()` —— 写回去

```python
df.to_csv('code/titanic_copy.csv', index=False)
```

**`index=False` 不能省。** 不加的话，pandas 会觉得「你那个名牌（`0 1 2 3...`）也是宝贵数据」，**把它当成一列写进文件**。下次读回来就莫名多一列（叫 `Unnamed: 0`），**12 列变 13 列**。

验证 —— 写完重读，看形状：

```python
df3 = pd.read_csv('code/titanic_copy.csv')
print(df3.shape)                 # → (891, 12) ✅
```

**验证依据**（比 shape 更硬的证据，直接看文件）：表头正好 12 个列名，且第一行第一格是 `1`（`PassengerId`）而不是 `0`（index）—— 名牌确实没进去。

> 🔍 顺带：文件里 `...7.25,,S` 那**两个连着逗号**，中间就是空的 `Cabin` —— `info()` 里那 687 个洞，物理上就长这样。

⚠️ **千万别写 `df = df.to_csv(...)`** —— `to_csv()` **不返回任何东西**（返回 `None`）。套上等号，`df` 这个名字就改指到 `None` 上去了；原表虽然还在内存里飘着，但**再没名字叫得到它**，下一行 `df.shape` 直接报错。

### 🔑 贯穿全局的一条规矩：**默认「造新的」，不动原来**

`set_index()` 不是「把 `df` 的 index 换掉」，是「照着 `df` **造一张新表**，它的 index 是 `Name`」。谁接住它，谁就是新名字：

```python
df2 = df.set_index('Name')       # 右边先造新表，左边后起名
print(df.head(3))                # df 的 index 还是 0 1 2 —— 从头到尾没被碰
```

跟 `x = 3 + 5` 一个道理：不能说「把 `x` 加了一下」，是 `3+5` **先算出 8**，`x` 才指过去。**先干活，后起名。**

> 📌 **pandas 里绝大多数操作，默认都是「造一张新的」，不动原来那张。**
> 所以会写一堆 `df2 = ...`、`df3 = ...` —— 不是啰嗦，是为了不把原始数据搞脏。

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
