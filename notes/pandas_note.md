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
| 2   | [03 选取筛选](https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/intro_tutorials/03_subset_data.html)                                                                                                                    | `loc`/`iloc`/布尔索引：筛出"女性且票价 > 30"          | ✅ 选列/筛行/loc/iloc 全跑通；筛出"女性且票价>30" = `(113, 12)` |
| 3   | [05 派生新列](https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/intro_tutorials/05_add_columns.html)                                                                                                                    | 向量化算 family_size、票价分箱（戒 for 循环）           | ✅ 向量化 / 新列 / `pd.cut` 分箱全跑通；321+321+181+53+NaN 15 = 891 |
| 4   | [06 汇总统计](https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/intro_tutorials/06_calculate_statistics.html)                                                                                                           | `groupby`：按舱位 × 性别算生存率                    | ✅ groupby 全跑通；size/count 拆出 891 / 714 / 177，生存率 女 0.742 男 0.189 |
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

**`index=False` 不能省。** 不加的话，pandas 会觉得「你那个名牌（`0 1 2 3...`）也是宝贵数据」，**把它当成一列写进文件**。下次读回来就莫名多一列，**12 列变 13 列**。

> ⚠️ **`index=True` 是默认值** —— 你什么都不写就是这个行为。
> 所以 `index=False` 不是「加一个设置」，是**关掉一个默认开着的东西**。
>
> 两个实跑验证过的细节：
> - 多出来的那列排在**最前面**（第 0 位），不是最后面：`['Unnamed: 0', 'PassengerId', ...]`
> - 它叫 **`Unnamed: 0`**（未命名第 0 个）—— 因为 index 自己没有名字，文件表头那个位置是**空的**。写出来的文件长这样：
>
> ```
>  ,PassengerId,Survived,Pclass,...      ← 开头那个孤零零的逗号 = 空表头
> 0,1,0,3,"Braund, Mr. Owen Harris",...  ← 开头这个 0 = 名牌混进数据里了
> ```

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

> **一句话**：`df[...]` 是**看菜下饭**的 —— 方括号里装**列名**，它去**取列**；装**真假表**，它去**筛行**。同一个方括号，两种人格。
>
> 🔗 对照：跟 ArcGIS 属性表里的「按属性选择」同一件事 —— 先写条件，再执行。

### 关键操作 ① 选列：单括号给「线」，双括号给「表」

```python
a = df["Age"]              # 单括号 → Series（一维）
print(a.shape)             # (891,)

b = df[["Age", "Sex"]]     # 双括号 → DataFrame（二维）
print(b.shape)             # (891, 2)

c = df[["Age"]]            # 双括号但只取一列
print(c.shape)             # (891, 1)  ← 还是两个数！
```

| 写法 | 拿到 | 形状 | 几个数 |
|---|---|---|---|
| `df["Age"]` | **Series**（一条线） | `(891,)` | 1 个 |
| `df[["Age"]]` | **DataFrame**（一张窄表） | `(891, 1)` | 2 个 |
| `df[["Age","Sex"]]` | **DataFrame** | `(891, 2)` | 2 个 |

**决定权在括号层数，不在取了几列。**

> 📌 **shape 里有几个数 = 这东西有几个维度。**
> 1 个数 = 一维，只有「长度」；2 个数 = 二维，「行 × 列」。
> `(891, 1)` 和 `(891,)` 是**两个不同的东西**，不是同一种东西的两种写法。

**那个逗号**：`(891,)` 里的逗号不是「还有个空位」，是 Python **单元素元组**的写法。

```python
(891)    # 就是数字 891，括号只是装饰
(891,)   # 只装了一个数的元组
```

**「取一列」和「取一行」—— 长度是交叉的：**

```python
print(df["Age"].shape)     # (891,)  ← 891 = 行数
print(df.iloc[0].shape)    # (12,)   ← 12  = 列数
```

取列，长度是**行数**；取行，长度是**列数**。**看形状里那个数从哪来，就知道它是行还是列。**

取一行拿到的是一张**竖过来的表** —— 列名跑到左边当了标签：

```
PassengerId                          1
Survived                             0
Pclass                               3
Name           Braund, Mr. Owen Harris
Age                               22.0
Cabin                              NaN
Name: 0, dtype: object
```

两个细节：

- **`dtype: object`** —— 一行里混着 `Name="Braund..."` 这种文字，**只要有一个格子是文字，整行就退化成 `object`**（对比 `df["Age"]` 是 `float64`：一列清一色数字）
- **`Name: 0`** —— Series 底下那个 `Name:` 在说「**我是从哪儿切下来的**」：切列写列名（`Name: Age`）、切行写行号（`Name: 0`）、`value_counts()` 写 `count`

### 关键操作 ② 筛行：**造名单 → 执行名单**

```python
mask = df["Age"] > 35      # ① 造名单
print(mask.shape)          # (891,)  ← 和原表一样长
print(mask.head())         # dtype: bool

above35 = df[mask]         # ② 执行名单
print(above35.shape)       # (217, 12)
```

**`mask` 不是「被显示出来」，是「被拿去执行」。**

```
mask 第 0 个 = False  →  第 0 行，扔
mask 第 1 个 = True   →  第 1 行，留  →  整行 12 列全带上
mask 第 2 个 = False  →  第 2 行，扔
```

**不是「用 True 换出一行」，是「True 决定这行留不留」。** 被留下的行，带着它的全部信息出来 —— `mask` 只管「留不留」，**不管「留哪几列」**。

**长度必须相等**：891 个答案对 891 行，一个答案管一行 —— 这就是先看 `mask.shape` 的原因，对不上就报错。

**`bool` 是第四种 dtype**（前三档是 `int64` / `float64` / `object`）：比较运算的结果只有两种可能，所以是 `bool`。

**筛完之后 index 会跳号：**

```
原表                     筛完（Age > 35）
0  Braund     22.0  ✗
1  Cumings    38.0  ✓  →   1  Cumings    38.0
2  Heikkinen  26.0  ✗
6  McCarthy   54.0  ✓  →   6  McCarthy   54.0
```

**一排房子，拆掉几间，剩下的门牌号不改。**

- ✅ **能查回去** —— 看到 index `6`，就知道是原表第 6 行。金融数据里这很关键（"这是哪一天、哪只股票"）
- ⚠️ **坑** —— `df[0]` 已经拿不到东西了（0 号被扔了）

### 关键操作 ③ 填洞：`notna()` / `isna()`

```python
mask2 = df["Age"].notna()   # "这格不是洞吗？"
df_no_hole = df[mask2]
print(df_no_hole.shape)     # (714, 12)  ← 就是 info() 里的 "Age 714 non-null"
```

`isna()` 是它的反面 —— "这格是洞吗？"

**洞在屏幕上显示为 `NaN`**（Not a Number）—— `Cabin` 列里那些 `NaN`，就是 `info()` 说的那 687 个洞。Day 1 是 pandas 告诉你的，Day 2 是你自己筛出来的。

### 关键操作 ④ 多重条件：`&` `|` `~`，每个条件自己裹括号

```python
mask3 = (df["Sex"] == "female") & (df["Fare"] > 30)
print(df[mask3].shape)      # (113, 12)
```

**括号为什么必须 —— 两个原因：**

**原因①：不能用 `and`。** `df["Sex"] == "female"` 给你的**不是单个 True/False，是 891 个**。`and` 一看这么多真值就懵了：

```
ValueError: The truth value of a Series is ambiguous
```

| 想说 | 不能写 | 要写 |
|---|---|---|
| 且 | `and` | **`&`** |
| 或 | `or` | **`\|`** |
| 非 | `not` | **`~`** |

**原因②：`&` 的优先级比 `>` 高**（跟「先乘除后加减」一个道理）。不加括号，Python 会先算 `"female" & df["Fare"]` —— 字符串和 Series 做与运算，当场爆炸。

> **口诀：`&` `|` `~` 两边，每个条件都自己裹一层括号。**

### 关键操作 ⑤ `loc` / `iloc` —— 两把钥匙

> **`loc` 用 index 里存的东西找；`iloc` 用「第几个」找。**
> `i` = **i**nteger，整数序号；没有 `i` 的那个，认名字。

| | `loc` | `iloc` |
|---|---|---|
| **行** | index 里的**值**（门牌） | **第几个**（从 0 数） |
| **列** | **列名**（字符串） | **第几列**（从 0 数） |
| 例子 | `df.loc[0, "Age"]` → `22.0` | `df.iloc[0, 5]` → `22.0` |

**行和列都不一样，别只记行的区别。**

**平时不分家**（原始 `df` 的 index 正好是 `0,1,2...`，和位置重合），**一分家就翻脸**：

| 场景 | index 变成什么 | `loc[0]` 还灵吗 |
|---|---|---|
| 原始 `df` | `0, 1, 2, 3...` | ✅ |
| **筛过**（`above35`） | `1, 6, 11, 13...` | ❌ `KeyError: 0` |
| **`set_index('Name')`**（Day 1 干过） | 人名 | ❌ 得写名字 |

实跑对照 —— 同一个 Cumings 先生，两条路：

```python
print(above35.iloc[0, 5])     # 第 0 个    → 38.0
print(above35.loc[1, "Age"])  # 门牌 1 号  → 38.0  ← 同一行
print(above35.loc[0, "Age"])  # 门牌 0 号  → KeyError: 0
```

**「第 0 个」≠「门牌 0 号」。**

**切片规则也不一样：**

| | `df.loc[0:2]` | `df.iloc[0:2]` |
|---|---|---|
| 拿到几行 | **3 行**（0、1、2） | **2 行**（0、1） |
| 规则 | 两头**都算**（数门牌：1 号到 3 号，3 号当然也算） | **不含右边**（数个数，跟 Python 列表一致） |

> 🔑 **记忆钩子（切片怎么记）**
>
> **「有 `i` 的 `iloc`，和 Python 列表用法一样。」**
>
> `i` = **i**nteger（整数下标），而 Python **列表**的下标也是整数 —— 同一套规矩：
>
> | | Python 列表 | `iloc` |
> |---|---|---|
> | 切片 `[0:2]` | 2 个，**不含右边** | **一样** |
> | 取负号 `[-1]` | 最后一个 | **一样**（`df.iloc[-1]` 能拿最后一行） |
>
> **所以只需要记住「`loc` 是那个特殊的」** —— `iloc` 不用记，它本来就跟你早会的列表一样。
>
> **为什么 `loc` 要特殊？** 因为它主要给**时间**用：
>
> ```python
> df.loc["2026-01-01":"2026-03-31"]     # 碳价数据，1月到3月
> ```
>
> 问「1 月到 3 月」，**3 月 31 号能不算上吗？** 不算上就反人类了。`iloc` 没这问题 —— 它数的是「第几个」，跟日期无关。

**什么时候用哪个**：明确知道要什么（某一天、某只股票）→ **`loc`，这是干活主力**；只是想看看（前 10 行）→ `iloc`。

### 关键操作 ⑥ 文字统计：换个问法 `value_counts()`

```python
print(df["Sex"].value_counts())
```

```
Sex
male      577
female    314
Name: count, dtype: int64
```

**不问「平均多少」，问「各有多少个」。** 577 + 314 = 891，一个不多一个不少。

- **自动按数量排序**（多的在上面）
- `dtype: int64` —— 数人头，不可能是 577.5 个
- 这还了 Day 1 欠的那道题：`describe()` 跳过文字列，是因为**文字没有平均值**

### 踩的坑

**① `import` 必须在用之前** —— Python 从上往下读。`import pandas as pd` 被 `#` 注释掉了，下面第 24 行用到 `pd` 就 `NameError`。同一文件里下面第 63 行有句好的 import，**远水救不了近火**。

**② 拼写错最阴** —— `tistanic.csv` ≠ `titanic.csv`。它不「看不懂」，它「**看起来对**」。报 `FileNotFoundError` 先看文件名拼写。

**③ 读报错的顺序：从下往上，只找自己的文件名**

```
KeyError: 0                                  ← ① 什么错（最底下）
File ".../pandas/_libs/index.pyx"...         ← ② pandas 内部，别看
File "...code/pandas_day1.py", line 97       ← ③ 你自己的代码在哪行
    print(above35.loc[0, "Age"])
```

中间那一大堆 `hashtable_class_helper.pxi` 是 pandas 在自言自语，跟你没关系。

**常见报错对照：**

| 报错 | 什么时候 |
|---|---|
| `KeyError` | `loc` 按门牌找不到（它是查字典，查不到就是"没这个键"） |
| `IndexError` | `iloc` 数位置越界 |
| `FileNotFoundError` | 路径/文件名不对 —— 先看提示符站在哪 + 拼写 |
| `NameError` | 名字没定义（多半是 `import` 被注释了） |
| `ValueError: truth value ... ambiguous` | 用了 `and`/`or` 而不是 `&`/`\|` |

## Day 3 · 派生新列（向量化）

> **一句话**：加新列不用一行行填 —— `df["新列"] = 整列算式`，pandas 替你逐行跑完。**站在等号左边，就是「写」。**
>
> 🔗 对照：ArcGIS 里的「添加字段 → 字段计算器」，一行一个值慢慢算。同一个活，pandas 一句话。

### 关键操作 ① 向量化：一列当整体算

```python
fs = df["SibSp"] + df["Parch"] + 1     # 兄弟姐妹 + 父母子女 + 自己
print(fs.shape)                        # (891,) ← 891 个一次算完
print(fs.head())
```

```
0    2
1    2
2    1
3    2
4    1
dtype: int64
```

**一行 `for` 都没写。** 换成普通 Python 写法长这样：

```python
fs_list = []
for i in range(len(df)):                                    # 4 行
    fs_list.append(df["SibSp"][i] + df["Parch"][i] + 1)
```

- **`+` 在这里是「两列相加」**，一行对一行（第 0 行配第 0 行，第 1 行配第 1 行）
- **`+1` 是把自己算进去** —— 一家几口人，不能把自己漏了
- **`fs` 是没名字的**：`fs.head()` 的输出里**没有 `Name:` 那一行**。因为 `SibSp` 和 `Parch` 名字不同，pandas 不知道该起什么名（Day 2 那些 `Name: Age` 是从原列切下来的，所以带名字）

> 🔑 **向量化是 pandas 的命根子。** 以后看到 `for` 循环在一行一行扫表，先问一句：**能不能整列算？**

### 关键操作 ② 新列诞生：等号左边 = 写

```python
df["family_size"] = fs
print(df.shape)                    # (891, 13) ← 12 列变 13 列
print(df["family_size"].head())    # Name: family_size, dtype: int64
```

**这是 Day 1 那条规矩的例外。** Day 1 说「默认造新的，不动原来」—— 那是**读**的时候。今天方括号跑到了**等号左边**。

> 🔑 **判据：看方括号在等号哪边。**
>
> | 写法 | 干什么 |
> |---|---|
> | `a = df["Age"]` | **读** —— 抽出 `Age` 给 `a`，`df` 纹丝不动 |
> | `df["family_size"] = fs` | **写** —— 在 `df` 上**新长出一列** |

写完它就归位了：能 `df["family_size"]` 取出来，`df.shape` 也变了，`head()` 里多一根。

### 关键操作 ③ 布尔列：`True` = 1，`False` = 0

```python
df["is_child"] = df["Age"] < 18
print(df["is_child"].dtype)      # bool
```

**命名惯例：`is_` / `has_` 开头** —— 一眼看出这列是「是非题」。

**布尔列能当数用：**

```python
print(df["is_child"].sum())        # 113
print(df[df["Age"] < 18].shape)    # (113, 13)
```

**两条路，同一个数。** `sum()` 把 `True` 当 `1` 加起来 —— 求和的本质就是**数人头**。

⚠️ 但这个 113 是「**有年龄记录** 且 小于 18」—— 见下面第一个坑。

### 关键操作 ④ `pd.cut` 分箱：连续数字 → 档次

```python
df["fare_level"] = pd.cut(
    df["Fare"],                            # 切哪一列
    bins=[0, 10, 30, 100, 600],            # 5 个切点 → 切出 4 段
    labels=["便宜", "中", "贵", "土豪"]       # 4 段，4 个名字
)
print(df["fare_level"].head())
```

```
0    便宜
1     贵
2    便宜
3     贵
4    便宜
Name: fare_level, dtype: category
Categories (4, object): ['便宜' < '中' < '贵' < '土豪']
```

手工核对：第 0 行票价 7.25 → `0 < 7.25 ≤ 10` → 便宜 ✅；第 1 行 71.28 → `30 < 71.28 ≤ 100` → 贵 ✅

**默认不含左边** —— 写成区间是 `(0, 10]`，圆括号那头不算。所以票价正好 = 0 的人，**落不进任何一段**。

**第五种 dtype 出现了：**

| dtype | 长什么样 | 什么时候学的 |
|---|---|---|
| `int64` / `float64` | 数字 | Day 1 |
| `object` | 随便什么文字 | Day 1 |
| `bool` | `True` / `False` | Day 2 |
| **`category`** | **有档次的分类** | **Day 3** |

**最妙的是最后那行 `Categories`：**

```
['便宜' < '中' < '贵' < '土豪']
         ↑ 它记住了顺序
```

> **`object` 是「一堆随便的文字」；`category` 是「有档次的分类」。**
>
> 那个 `<` 号是 pandas 在说：**我知道这四档谁大谁小** —— 顺序就是你 `labels` 里的先后。以后排序会按「便宜 → 中 → 贵 → 土豪」走，不会按拼音乱排。
>
> 顺带**省内存**：891 个格子只有 4 种值，pandas 内部只存编号，不重复存 891 遍汉字。

### 踩的坑

**① `NaN` 跟任何数比较，一律得 `False`**

`Age` 列有 177 个洞。`df["Age"] < 18` 遇到洞不报错，**老老实实返回 `False`**。

所以 `df["is_child"].sum()` = 113，指的是「**有年龄记录** 且 小于 18」的人数 —— 那 177 个洞被静悄悄排除在外了。

> ⚠️ **筛之前先 `info()` 看有没有洞。** 少了多少行，心里得有数。

**② `value_counts()` 默认把洞藏起来**

```python
print(df["fare_level"].value_counts())
```

```
便宜    321
中     321
贵     181
土豪     53
```

**加起来 876，不是 891。少了 15 个。**

那 15 位票价 = 0 的乘客掉出了 `bins`、变成了 `NaN` —— 但 `value_counts()` 一个字没说。

加个参数就能看见：

```python
print(df["fare_level"].value_counts(dropna=False))
```

```
便宜     321
中      321
贵      181
土豪     53
NaN     15      ← 藏起来的 15 个
```

321 + 321 + 181 + 53 + 15 = **891** ✅

> 🔑 **跟 `info()` 不一样**：`info()` 主动报告「714 non-null，有 177 个洞」；`value_counts()` **默认闭嘴**（参数叫 `dropna=True`）。
>
> **「统计了 891 个」和「给你看了 876 个」是两回事。**

**③ 昨天那个数对上了，今天这个数差点没对上** —— Day 2 的 `value_counts()` 是严丝合缝的 891，所以今天看到 876 时**要自己起疑**。**能加得上的数才是可信的数。**

## Day 4 · 汇总统计（groupby）

> **一句话**：**「按 ___ 分，算 ___」** —— `groupby` 把一张表**拆成几堆**，每堆各算各的，再拼回来。
>
> 🔗 对照：ArcGIS 属性表里的「Summary Statistics」—— 选一个**分类字段**，再选一个**统计字段**。你早就干过，只是换了个写法。

### 关键操作 ① 从「一个数」到「一堆数」

```python
print(df["Age"].mean())                      # 不分：一个数 → 29.69911764705882
print(df.groupby("Sex")["Age"].mean())       # 按 Sex 分：两个数
```

```
Sex
female    27.915709
male      30.726645
Name: Age, dtype: float64
```

**「按什么分」的那个东西，分完就成了每行的姓名牌。** 门牌从 `0, 1, 2...` 变成了 `female` / `male`。

跟 Day 2 的 `value_counts()` 对照：

| | 门牌 | `Name:` | 顺序 |
|---|---|---|---|
| `value_counts()` | male / female | `count` | 按**数量**（577 > 314） |
| `groupby("Sex")` | female / male | `Age` | 按**字母序** |

**`value_counts()` 只能数人头；`groupby` 想算什么算什么** —— 这就是它多出来的本事。

### 关键操作 ② 拆开看：`size()` vs `count()`

```python
print(df.groupby("Sex")["Age"].size())     # 每堆几行
print(df.groupby("Sex")["Age"].count())    # 每堆有几个「有值」的
```

```
size()   →  female 314   male 577     合计 891
count()  →  female 261   male 453     合计 714
差       →  female  53   male 124     合计 177
```

**三个数全对上了** —— 891 是 Day 2 `value_counts()` 那个数，714 和 177 是 Day 1 `info()` 里的 `Age 714 non-null` 和那批洞。

| | 数什么 |
|---|---|
| `size()` | 这堆**一共几行**（管你有没有洞） |
| `count()` | 这堆里**有几个「有值」的**（洞不算） |

> 🧠 **`groupby` 的真正本事：把「一个总数」拆成「一堆分项」。**
>
> Day 1 只知道「**有** 177 个洞」；今天知道「洞**在哪**」—— 女 53、男 124。
>
> 而且**分项加起来必须等于总数**。对上了，说明你分对了 —— **这是最好的自检。**

### 关键操作 ③ 0/1 列的平均 = 比率

```python
print(df.groupby("Sex")["Survived"].mean())
```

```
Sex
female    0.742038
male      0.188908
Name: Survived, dtype: float64
```

**`Survived` 只有 0（没活）和 1（活了）** —— 所以它的平均，就是**活下来的比例**，也就是**生存率**。

Day 3 那句「`True` 就是 1，`False` 就是 0」，在这儿结出了果。

### 关键操作 ④ 多列分组：门牌分两层

```python
print(df.groupby(["Sex", "Pclass"])["Survived"].mean())
```

```
Sex     Pclass
female  1         0.968085
        2         0.921053
        3         0.500000
male    1         0.368852
        2         0.157407
        3         0.135447
Name: Survived, dtype: float64
```

- **方括号里变成列表** —— 因为要按**两样**分
- **门牌分了两层**（叫 **MultiIndex**）：外层 `Sex`，内层 `Pclass`。`female` 只写一次，下面两行空着 —— 那是 pandas 在说「**沿用上面的**」
- **谁在外层，看你列表里的先后** —— `["Sex", "Pclass"]` 先 Sex 后 Pclass

**为什么要按两样分？看这组对比：**

| | 只按性别 | 按性别 × 舱位 |
|---|---|---|
| **女性** | **0.742** | 头等 **0.968** ／ 二等 0.921 ／ 三等 **0.500** |
| **男性** | 0.189 | 头等 0.369 ／ 二等 0.157 ／ 三等 0.135 |

> 💡 **`0.742` 这个数，把 `0.968` 和 `0.500` 平均掉了。**
>
> 同样是女性，**头等舱和三等舱的生存率差了一倍**。只按性别分组，这个差别**根本看不见**。
>
> **分组分得越细，被平均值掩盖的东西就越少。**

**而且能反着拼回去** —— 6 个分项按各自人数加权，正好合回 `0.742` 和 `0.189`。就是刚才那 177 个洞的同一条道理：**分项加起来必须等于总数。** 想自己验：

```python
print(df.groupby(["Sex", "Pclass"])["Survived"].size())   # 每堆几个人
```

### 踩的坑

**① `.mean()` 默认跳过洞** —— `df["Age"].mean()` = 29.699，是 **714 个人**的平均，不是 891 个。参数叫 `skipna=True`，**跳过而且不告诉你**。

**② 「洞」这个主题，今天第三次出现：**

| 什么时候 | pandas 对洞做了什么 |
|---|---|
| Day 3 · `df["Age"] < 18` | 洞比出 `False`，**悄悄排除** |
| Day 3 · `value_counts()` | 洞**藏起来不显示** |
| Day 4 · `.mean()` | 洞**跳过不参与计算** |

> 🧠 **规律：pandas 遇到洞的默认动作是「静悄悄跳过」。** 不报错、不警告、不提醒 —— **你得自己知道它在跳。**

**③ `groupby` 的门牌顺序和 `value_counts()` 不一样** —— 一个按**字母序**（female 在前），一个按**数量**排（male 在前）。别因为它俩数字一样就以为是一回事。

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
