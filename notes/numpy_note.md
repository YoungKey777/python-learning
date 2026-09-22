# **numpy** 学习笔记

> 记录方法：跟官方 user guide，每篇学完**关掉网页**，用自己的话写、在自己的数据上重敲一遍
> 来源：numpy 官方 user guide（**stable 版文档**，对应本机 numpy 2.2.6）
> - 入口：https://numpy.org/doc/stable/user/absolute_beginners.html（绝对初学者指南）
> - 环境：Python 3.10.9 + numpy 2.2.6 + pandas 2.3.3
> - 🔗 **这份笔记的定位**：pandas 的 `Series` 和 `DataFrame` **底下就是 numpy 的数组**。pandas 你已经学到 Day 6 了，所以这一轮不是「学新东西」，是**往回挖** —— 把你已经用过的那些 pandas 操作，掀开盖子看看底下发生了什么

---

## 🧭 路线（5 天，每天约 40~60 分钟）

| 天   | 读什么                                                                                                     | 当天练习                                                             | 状态                                                                    |
| --- | ------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | --------------------------------------------------------------------- |
| 1   | [绝对初学者指南](https://numpy.org/doc/stable/user/absolute_beginners.html)                                   | 从 list 造数组 → 看 `.shape` / `.dtype` / `.ndim`；把 titanic 的 DataFrame 和 Series **脱壳**成数组 | ⬜                                                                     |
| 2   | 同上（Indexing and slicing 那节）+ [quickstart](https://numpy.org/doc/stable/user/quickstart.html)             | 一维/二维切片、`a[:, 0]`、`a[0:2, 1:3]`、布尔索引 `a[a > 5]`                   | ⬜                                                                     |
| 3   | [广播规则](https://numpy.org/doc/stable/user/basics.broadcasting.html)                                      | `a + 1`、数组加数组、`(3,4)` 加 `(4,)`；拿 `df["Fare"] * 1.1` 对照           | ⬜                                                                     |
| 4   | 绝对初学者指南（Aggregation / 数学那几节）                                                                            | 一维 `sum/mean/std`；**二维 `axis=0` vs `axis=1` 各得到什么形状**             | ⬜                                                                     |
| 5   | [随机数生成器](https://numpy.org/doc/stable/reference/random/generator.html)                                   | **量化那一组**：日收益率 → `np.diff` / `np.log` / `np.cumprod` / 年化波动率 / `np.cov` | ⬜                                                                     |

**每天固定动作**（跟 pandas 一样）：

1. 读当天那节（十几分钟）
2. **关掉网页**，在 `code/numpy_dayN.py` 里边敲边跑，不许复制粘贴
3. 在下面填当天小节 → 每天一个脚本，不要堆在一个文件里

### 五天各挖什么（一句话版）

| 天 | 掀开哪个盖子 | 你会认出什么 |
|---|---|---|
| 1 | **数组是什么** | pandas 的 `.shape` / `.dtype` **就是从 numpy 借来的** —— 不是 pandas 自己发明的 |
| 2 | **索引** | `df.iloc[:, 0]` 就是 `a[:, 0]`；`df[mask]` 就是 `a[mask]`。**`iloc` 的 `i` 就是「numpy 式」的意思** |
| 3 | **广播** | Day 3 那个「家庭人数 = `SibSp` + `Parch` + `1`」，**那个 `+1` 就是广播** |
| 4 | **轴（axis）** | pandas 里最容易搞反的参数 —— `axis=0` 压掉行、剩下列 |
| 5 | **量化那一组** | 收益率、复利、年化波动率、相关系数矩阵 —— **直接对接 roadmap 阶段 5 / 6** |

- **挂账**：numpy 官方没有 pandas 那样的「Getting Started 8 篇」系列，所以这 5 天是**按量化需要倒推的**，不照抄目录。遇到用不上的（`np.meshgrid` / 结构化数组 / IO），直接跳
- **验收（第 5 天自测）**：不看资料写出 —— `a[:, 0]` 和 `a[0, :]` 分别是什么；`axis=0` 和 `axis=1` 分别在压哪个方向；用 `np.random` 造 250 天收益率，算出**累计净值曲线**和**年化波动率**

### 数据从哪来

**不用下载任何东西**，两种来源就够：

- **真数据**：`pandas/data/titanic.csv`（已经在本机，Day 1~3 拿它脱壳）
- **假数据**：`np.random` 现场造（Day 5 造收益率，比真行情更可控）

---

## Day 1 · ndarray 是什么

> 待填：一句话 / 3 个关键操作 / 踩的坑

## Day 2 · 索引切片

> 待填：一句话 / 3 个关键操作 / 踩的坑

## Day 3 · 广播（broadcasting）

> 待填：一句话 / 3 个关键操作 / 踩的坑

## Day 4 · 聚合与轴（axis）

> 待填：一句话 / 3 个关键操作 / 踩的坑

## Day 5 · 量化那一组（收益率 / 复利 / 波动率 / 协方差）

> 待填：一句话 / 3 个关键操作 / 踩的坑

---

## 🔧 环境与坑（随时追加）

- **numpy 版本**：本机 2.2.6（`python -c "import numpy; print(numpy.__version__)"` 可查）
- **文档版本要对齐**：numpy.org 默认打开的是 `stable`，与 2.2.6 一致；别看 `dev` 版（那是未发布的开发版）
- **`np.random` 的新写法**：老教程里的 `np.random.seed(42)` 已经**不被推荐**，新写法是 `rng = np.random.default_rng(42)`（Day 5 会用）。老写法还能跑，但别学
- **`import pandas as pd` 之后你早就在用 numpy 了** —— pandas 是建在 numpy 上的，`df["Age"].mean()` 最后是 numpy 在算

---

*所属模块：[[python-for-quant/roadmap|roadmap]] 阶段 2（numpy + pandas）；上游 [[notes/python_note|python_note]]，姊妹篇 [[notes/pandas_note|pandas_note]]*
