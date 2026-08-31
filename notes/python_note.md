# **Python** 学习笔记

> 记录方法：边读官方教程边动手练，学到什么记什么，用自己的话写
> 来源：Python 官方教程
> - 中文版：https://docs.python.org/zh-cn/3/tutorial/
> - 英文版：https://docs.python.org/3/tutorial/

## 1. 课前甜点：Python 是什么

**一句话**：简单 + 强大——能自动处理文件，能写大型程序，跨 Windows/macOS/Linux，上手快、代码短。

### 它和别的工具的区别

| 对比对象 | 结论 |
|---|---|
| shell 脚本 / 批处理 | shell 只擅长移动文件、改文本，写不了复杂应用（GUI、游戏）；Python 是完整编程语言 |
| C / C++ / Java | 编译→运行循环太慢；Python 是**解释型**，写完立刻能跑，改一行马上看结果 |

### 三个关键特点（会影响写码习惯）

1. **缩进是语法**：用缩进代替大括号分块代码，缩进错了直接报错
2. **不用声明变量类型**：`x = 5` 直接写（C 里要 `int x = 5`）
3. **标准库丰富 + 生态模块**：I/O、网络、GUI 内置；以后要学的 pandas、akshare 就是"装模块"——Python 最值钱的资产

### 其他

- **可扩展**：性能关键的部分可以用 C 扩展（暂时用不上，知道即可）
- 名字来自 BBC 喜剧 "Monty Python 飞行马戏团"，**与蟒蛇无关** 🐍

### 对我的意义

- 解释型 → "写→跑→改"循环很快，正适合以后做因子研究、回测的快速试错节奏
- 先学核心、用到再补（roadmap 路线），标准库/模块正是"用到再补"的落点

### 动手练习

在 VS Code 终端（Ctrl+`）输入 `python` 回车进入交互模式，试：
- `print("hello")`
- `1 + 1`
- `"量化" + "学习"`

输入 `exit()` 退出。

---

## 2. 使用 Python 的解释器

### 2.1 唤出解释器

- **启动**：终端输入 `python`（Windows 还有 `py` 命令；Mac/Linux 是 `python3`）
- **退出**：输入 `quit()`（或 Windows 按 Ctrl+Z 再回车，Mac/Linux 按 Ctrl+D）
- 小技巧：交互模式下按 Ctrl+P 可以调出上一条命令（少敲几遍）

### 2.1.1 传入参数

跑脚本时可以在命令后面带参数：

```
python test.py a b c
```

这些参数会存进 `sys.argv` 列表（第 0 个元素是脚本名本身）：

```python
import sys
print(sys.argv)
```

输出 `['test.py', 'a', 'b', 'c']`。现在了解即可，以后写"接收参数的脚本"时会用到。

### 2.1.2 交互模式

- 主提示符 **`>>>`**：等你输入一行命令
- 次提示符 **`...`**：多行语句还没输完，继续敲
- 例子（注意 `if` 行尾的**冒号** + 下一行开头的**缩进**，缩进是语法）：

```
>>> the_world_is_flat = True
>>> if the_world_is_flat:
...     print("Be careful not to fall off!")
...
Be careful not to fall off!
```

### 2.2 解释器的运行环境

#### 2.2.1 源文件的字符编码

- 源码默认 **UTF-8**：中文注释、中文字符串直接写，**不用声明任何东西**——对中文用户是白送的一条
- `# -*- coding: xxx -*-` 声明只在特殊编码时才需要，正常完全不用管
- 文件保存为 UTF-8（VS Code 默认就是）

### 动手练习

1. 终端输入 `python`，把上面 `if` 示例原样敲一遍（看到 `...` 别慌，是"还没输完"）
2. 输入 `quit()` 退出
3. 写一个 `test.py`：`import sys; print(sys.argv)`，用 `python test.py 1 2 3` 跑一次，看输出
4. 把同样代码写成 .py 文件跑一遍，对比"交互模式"和"脚本模式"两种运行方式

---

## 3. Python 速览

### 例子的格式约定（章首说明，读教程必备）

| 例子里 | 含义 |
|---|---|
| `>>>` 开头的行 | **你自己敲**的内容（只敲提示符后面的部分） |
| 没有提示符的行 | **电脑的输出**，不用敲 |
| 多行语句末尾的空行 | 敲一个空回车表示"语句结束" |

提示：网页右上角点 `>>>` 可以隐藏提示符，方便把输入行整段复制到自己终端。

> 对笔记的意义：在 VS Code 里写 .py 文件没有提示符这回事，这条主要用来**读教程时别把输出行也抄进代码**。

### 注释

- `#` 到行尾 = **注释**：写给人看的，Python 完全忽略
- 位置随便：行开头、代码后面、单独一行（前面有空格也行）
- 例外：**字符串里面的 `#` 是普通字符**，不算注释

```python
# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# 引号里的 # 是普通字符"   # 这里开始的才是注释
```

> 中文注释随便写（UTF-8 默认）——养成写注释的习惯，是给三个月后的自己看的。

**多行注释**：Python 没有专用语法，三选一：
1. **VS Code 快捷键 Ctrl+/**：选中多行批量加/去 `#`（日常最常用）
2. 每行一个 `#`
3. `"""三引号"""` 看着像多行注释，**其实是字符串**——但写在函数/类开头就是正式文档 docstring，Python 会保存它（以后写函数用）

### 3.1 使用 Python 作为计算器

#### 3.1.1 数字

- 两种类型：**`int`**（整数：`2`、`4`、`20`）和 **`float`**（小数：`5.0`、`1.6`）
- **除法 `/` 总是返回浮点数**：`4 / 2` → `2.0`（不是 `2`！）
- `//` 整除（只取整数部分）：`17 // 3` → `5`
- `%` 取余数：`17 % 3` → `2`
- `**` 乘方：`5 ** 2` → `25`
- **混合类型运算自动转 float**：`4 * 3.75 - 1` → `14.0`
- **变量必须先赋值再用**，否则报错 `NameError`（踩过坑 ✅）

```python
width = 20   # 赋值
17 // 3      # 5
17 % 3       # 2
5 ** 2       # 25
```

#### 3.1.2 字符串

**引号与转义**
- 单引号 `'...'` 和双引号 `"..."` 结果相同，随意选
- 反斜杠 `\` 用于转义：`\n` 换行、`\'` 打印单引号等
- **原始字符串** `r"..."`：前置 `r`，`\` 不再转义（如路径、正则里常用）

**合并与重复**
- `+` 合并（粘到一起）：`'Py' + 'thon'` → `'Python'`
- `*` 重复：`'py' * 3` → `'pypypy'`
- **相邻字符串字面量自动拼接**（排版神器）：括号里换行，Python 自动粘成一个，且不产生换行符

```python
text = ('第一段 '
        '第二段')    # → '第一段 第二段'
```

> 注意：相邻拼接只对"直接写出来的字符串"有效；变量拼接要用 `+`。

**索引（下标）**
- 第一个字符索引是 **0**：`word[0]` 是第一个
- **负数索引从右边数**：`word[-1]` 是最后一个

```
>>> word = 'Python'
>>> word[-1]   # 'n'
>>> word[-2]   # 'o'
```

**切片**
- `word[a:b]`：取从 a 到 b 之间（**含 a 不含 b**）
- 索引指向字符**之间**：

```
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```

- `word[:2]` 从头切到 2、`word[2:]` 从 2 切到结尾、`word[-2:]` 取最后两个

**不可变 immutable**
- 字符串**不能改**：`word[0] = 'X'` 会报错
- 想改就重新造一个新字符串（切片组合）

#### 3.1.3 列表

- 方括号 + 逗号：`squares = [1, 4, 9, 16, 25]`
- **索引、切片和字符串一模一样**：`squares[0]`、`squares[-1]`、`squares[-3:]`
- `+` 加号可以合并两个列表
- `append()` 在末尾添加新元素：`squares.append(36)`
- **可变 mutable（和字符串的最大区别）**：`squares[0] = 36` 可以改
- **嵌套列表**：列表里装列表

```python
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]      # [['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]            # ['a', 'b', 'c']
>>> x[0][1]         # 'b'
```

**记忆点**：字符串不可变 vs 列表可变——改了会不会报错，是区分两者的关键。

### 3.2 走向编程的第一步

#### for 循环（发牌，不数数）

- Python 的 for **不数数**（不像 C 的 `for i = 0; i < 10`），而是**逐个拿元素**：列表里有几个就处理几次
- `len(东西)` = 数它有几个元素
- `print(w, len(w))` 一次打印多个，逗号隔开自动空格

```python
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# cat 3
# window 6
# defenestrate 12
```

#### 遍历中修改集合（容易踩坑 ⚠️）

- **for 只认位置不认人**：循环按"座位号"叫号，删除元素会让后面的人前移换座，而 for 不会回头再叫——**有人被跳过，且不报错**
- 列表：悄悄错（跳过元素）；字典：直接报错（`RuntimeError: dictionary changed size during iteration`）
- 解法就一条：**循环跑的对象 ≠ 修改的对象**

```python
# 写法 A：想"删" → 循环跑在副本上
for w in words.copy():
    if w != '林业':
        words.remove(w)

# 写法 B：想"挑出来另存" → 装进新容器
forest_words = []
for w in words:
    if w == '林业':
        forest_words.append(w)
```

（练习记录见 4.2）

#### 按索引迭代：range() + len()

需要"位置"（第几个）时用，`i` 是座位号，`a[i]` 是座位上的人：

```python
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

# 0 Mary
# 1 had
# 2 a
# 3 little
# 4 lamb
```

---

## 4. 更多控制流工具

### 4.1 if 语句

- **从上往下试，命中一个就停**：`if` → `elif`（可以多个）→ `else`（兜底，可选）
- 注意行尾**冒号** + 下一行**缩进**（缩进是语法）
- `input("提示语")` 等待用户输入，**返回的是字符串**，要当数字用先 `int(...)` 转换

```python
x = int(input("please enter an integer:"))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
```

### 4.2 for 语句（我的练习记录）

```python
# for 迭代：发牌，逐个拿
words = ['林业', '遥感', '碳汇']
for w in words:
    print(w, len(w))

# 直接删 → 踩坑：删掉之后会补位，后面的元素被跳过（不报错但结果错！）
words = ['林业', '遥感', '碳汇']
for w in words:
    if w != '林业':
        words.remove(w)
print(words)
# ['林业', '碳汇']   ← '碳汇'没删掉，因为删除后它前移换座，for 不回头叫

# 解法 1：复制快照，循环跑在副本上
words = ['林业', '遥感', '碳汇']
for w in words.copy():
    if w != '林业':
        words.remove(w)
# ['林业']

# 解法 2：反向，符合的抓进新列表
words = ['林业', '遥感', '碳汇']
forest_words = []
for w in words:
    if w == '林业':
        forest_words.append(w)
print(forest_words)   # ['林业']
print(words)          # 原列表没动
```

### 4.3 range() 函数

- 生成等差数列，**永远不含终止值**：

```python
range(5)             # 0 1 2 3 4
range(5, 10)         # 5 6 7 8 9       （起点, 终点）
range(0, 10, 3)      # 0 3 6 9         （起点, 终点, 步长）
range(-10, -100, -30)  # -10 -40 -70   （步长可以为负）
```

- **range() 不等同于列表**：它是"提货单"不是"实货"——不真造出所有数字，**要一个给一个**（惰性），省空间
- `print(range(10))` 只会显示 `range(0, 10)`（打印的是凭证本身）
- `list(range(10))` = 把提货单一次性提光，变成真列表

```python
print(range(10))       # range(0, 10)   ← 提货单
print(list(range(10))) # [0, 1, 2, ..., 9]  ← 真货
```

### 4.4 break 和 continue（循环控制）

- **`break` = 立即结束整个循环**：找到答案就收工，不白费力气
- **`continue` = 跳过本次剩余代码，进入下一次**：某类情况不用处理，其他照常
- **if + continue = 安检门**：if 成立 → 撞上 continue → 本轮后面全部跳过，直接下一轮；if 不成立 → 继续往下走（对比实验跑过 ✅）

```python
# break：找到第一个因数就停（不用再试更大的数）
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break

# 4 equals 2 * 2
# 6 equals 2 * 3
# 8 equals 2 * 4
# 9 equals 3 * 3
```

```python
# continue：偶数打印完直接跳，奇数走下面那行
for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")
```

**顺带：f-string**：`f"值 = {变量}"`，引号里 `{}` 放变量/表达式，自动把值填进去——以后 print 天天用。

**一句话区分**：break 是"退队"，continue 是"插队到下一个"。

### 4.5 循环中的 else

- 规则：**循环正常跑完（没被 break 打断）才执行 else；被 break 打断就不执行**
- 用途：else 当"完成信号"——break = 中途放弃，自然跑完 = 使命完成

```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "等于", x, "*", n//x)
            break
    else:
        print(n, "是质数")   # 只有全程没 break 的才会走到这
```

### 4.6 pass 语句（占位符）

- **不执行任何动作**，作用就是"占个位置"——Python 要求 if/for/def/class 后面必须有代码块，**不能空着**（空着报 `IndentationError`）
- 三种用法：
  1. **占位**：先搭函数/类骨架，逻辑以后填（"先骨架后填肉"的开发节奏）

     ```python
     def initlog(*args):
         pass    # 记得实现这个！

     class MyEmptyClass:
         pass
     ```

  2. **空转**：循环里没有要做的动作

     ```python
     while True:
         pass    # 无限等待 Ctrl+C 中断
     ```

- 占位也可以写 `...`（三个点，传统占位符号），无特殊含义，随习惯

### 4.7 match 语句（模式匹配）

**一句话**：switch 的升级版——不仅按值找分支，还能从匹配对象里**拆出值绑给变量**。

**执行规则**：从上往下试，**第一个匹配的 case 才执行**；全不匹配则什么都不做；`case _` = 通配符（必定匹配，兜底）。

**必学四件套**：

```python
# ① 字面值匹配 + _ 通配符（= switch 用法）
match status:
    case 400:
        return "Bad request"
    case _:
        return "Something's wrong"

# ② | 组合（"或"）
case 401 | 403 | 404:
    return "Not allowed"

# ③ 变量绑定（match 的灵魂）：匹配的同时把值装进变量
match point:                    # point = (0, 5)
    case (0, 0):
        print("Origin")
    case (0, y):                # 第二个值自动装进 y
        print(f"Y={y}")         # Y=5
    case (x, y):
        print(f"X={x}, Y={y}")

# ④ 守卫子句：匹配后还要过一道 if 检查
case Point(x, y) if x == y:
    print(f"Y=X at {x}")
```

**了解**：嵌套模式 `case [Point(0, y1), Point(0, y2)]`。
**待学完类再回看**：类模式 `case Point(x=0, y=0)`（按属性匹配，配 `__match_args__`，依赖 class/self 知识）。

**用到再查**：映射模式 `{"k": v}`、扩展解包 `[x, y, *rest]`、`as` 捕获、enum 具名常量（必须带点号）、True/False/None 按 id 比较。

**阅读心法**：把每个 case 当"带空格的模板"，变量名是空格——匹配成功时自动被填上主语的值（同解包赋值）。

### 4.8 定义函数

**定义 vs 调用**（踩过坑 ✅）：
- `def 名字(参数):` 只是**写菜谱**，不执行
- **调用** `名字(参数)` 才真正执行函数体
- `return` 把结果**递出**厨房——但递出来 ≠ 显示出来，.py 里要自己 `print()` 接住

```python
def add(a, b):
    return a + b

print(add(3, 5))    # 调用 + 打印 → 8
```

**docstring（文档字符串）**：函数第一行的三引号字符串 = 产品说明书
- `help(函数名)` 自动显示它；VS Code 鼠标悬停也能看；`函数名.__doc__` 可访问
- `#` 注释**运行前就被丢弃**，工具读不到——这是 docstring 和注释的本质区别
- 分工惯例：docstring 面向使用者（这函数**干什么**），`#` 面向读源码的人（这段**为什么**这么写）

```python
def add(a, b):
    """计算 a 加 b，返回结果。"""
    return a + b
```

**作用域（变量住在哪 + 怎么找）**：
- 三个住处：**局部**（函数内）、**全局**（文件顶层）、**内置**（print/len 等自带）
- 查找顺序从里往外：**局部 → 全局 → 内置**（先翻自己屋，再去图书馆，最后用自带的）
- 关键规则：**函数内"读"全局可以；"赋值"= 在自己屋里新造一个局部变量，全局不变**（新手大坑 ⚠️）

```python
x = 10

def show():
    print(x)       # 读全局 → 10 ✅

def change():
    x = 20         # ❌ 不是改全局，是造了个新的局部 x
    print(x)       # 20（局部那个）

change()
print(x)           # 还是 10
```

- 想改外面数据 → **用 return 递出**，外面自己接住赋值（干净写法）

```python
def add_one(value):
    return value + 1

x = add_one(x)     # 外面接住 → 11
```

- `global` / `nonlocal` 声明：认识即可，日常不用（读到别人代码不慌）

### 4.9.1 默认参数值

- 定义时给参数默认值，**调用时可以少传**：`def f(a, b=1)` → `f(5)` 也能跑（b 自动用 1）
- 规矩：**必选参数在前，带默认值的在后**
- 三种调用方式：

```python
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('Do you really want to quit?')                    # 只给必选
ask_ok('OK to overwrite the file?', 2)                   # 给前两个
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')  # 全给
```

- **位置参数只能从左到右连续给**，不能跳；想给第 1、3 个（跳过第 2 个）→ 用关键字参数（4.9.2 学）：

```python
ask_ok('OK?', reminder='Come on!')   # 跳过 retries，指名道姓给 reminder
```

- 坑 ⚠️（教程末尾的警告）：**默认值只在函数定义时求值一次**——不要用可变对象（如 `[]`）当默认值，会被多次调用共享、累积脏数据：

```python
def f(a, lst=[]):     # ❌ 默认列表被所有调用共享
    lst.append(a)
    return lst

print(f(1))           # [1]
print(f(2))           # [1, 2]  ← 累积了！

# ✅ 正确写法：默认 None，函数内再建新列表
def f(a, lst=None):
    if lst is None:
        lst = []
    lst.append(a)
    return lst
```

### 4.9.2 关键字参数（指名道姓传参）

- `kwarg=value` 形式：**按名字传，不按位置**——可以乱序、可以跳过中间参数、可读性好

```python
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    ...

parrot(1000)                                       # 位置参数
parrot(voltage=1000)                               # 关键字参数
parrot(action='VOOOOOM', voltage=1000000)          # 乱序 OK
parrot('a thousand', state='pushing up the daisies')  # 位置 + 关键字混用
```

- **规矩**：
  1. 位置参数在前，关键字参数在后（`f(1, b=2)` ✅；`f(b=2, 1)` ❌）
  2. **一个参数只给一次值**（`function(0, a=0)` ❌ → 报错 `TypeError: got multiple values for argument 'a'`，即"a 收到了多个值"）
  3. 名字必须和定义时一致（`f(actor='x')` ❌ 未知关键字）
  4. 必选参数躲不掉，但**可以用关键字传**：`parrot(voltage=1000)` ✅
- **一段话版**：位置在前、关键字在后；名字要对得上；一个参数只能给一次值；必选参数用哪种传法都行；关键字之间顺序随便。

### 4.9.3 特殊参数（/ 和 *，划定传法边界）

```
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      └──┬───┘    └────┬────┘   └──┬───┘
      仅限位置      位置或关键字   仅限关键字
```

- **`/` 左边**：仅限位置（不能当关键字传）
- **`*` 右边**：仅限关键字（不能按位置传）
- 中间：随便（默认）
- 记法：**斜杠左边只排队，星号右边只点名**

```python
def pos_only(arg, /):      # arg 只能按位置
    pos_only(1)            # ✅
    pos_only(arg=1)        # ❌ TypeError

def kwd_only(*, arg):      # arg 只能按关键字
    kwd_only(3)            # ❌ TypeError
    kwd_only(arg=3)        # ✅
```

- 用途：作者有意限制传法，避免歧义（如 `sorted(数据, *, key=...)` 的 key 只能关键字传）
- 教程末尾 `foo(name, **kwds)` 冲突例子：等学完 `**kwds`（4.9.4）再回看，知道"`/` 能解决名字冲突"即可

#### 4.9.3.5 小结（什么时候用）

- **仅限位置 `/`**：形参名没意义时（调用方不需要知道名字）、强制顺序时、设计 API 想防未来改参数名造成破坏时
- **仅限关键字 `*`**：形参名有意义、显式写名字能让调用更易懂时
- 设计 API 时才考虑这些；自己写内部小函数，用默认"位置或关键字"即可

### 4.9.4 任意实参列表（*args / **kwargs）

- **`*args`**：收集**多余的位置参数** → 元组（来几个收几个）
- **`**kwargs`**：收集**多余的关键字参数** → 字典（键 = 参数名）
- 完整形态顺序固定：**必选 → `*args` → `**kwargs`**

```python
def total(*args):              # 传几个都行
    return sum(args)

total(1, 2, 3, 4)              # 10

def show_info(**kwargs):
    print(kwargs)

show_info(名称="林业", 年份=2026)
# {'名称': '林业', '年份': 2026}

def func(必选, *args, **kwargs):   # 完整形态
    ...
```

- 用途：不知道调用者传几个参数、包装/转发函数（装饰器的基础）、收配置项
- 惯例：名字固定 `args` / `kwargs`（能改名，但别改）
- **`*args` 后面的参数只能是仅限关键字**：`def concat(*args, sep="/")` → `sep` 只能 `concat(..., sep=".")` 这样传
- 回看 4.9.3 的 `foo(name, **kwds)` 冲突例子：`/` 让 name 变成仅限位置，`**kwds` 里的 `'name'` 键就不会撞车了

### 4.9.5 解包实参列表（调用时拆开）

**记忆点：定义时 `*` = 打包（吸进来），调用时 `*` = 拆包（放出去）——方向相反。**

```python
# 调用时 *：把列表/元组拆开，当独立位置参数
args = [3, 6]
list(range(*args))     # range(3, 6) → [3, 4, 5]

nums = [1, 2, 3]
print(*nums)           # 1 2 3（拆开）
print(nums)            # [1, 2, 3]（不拆）

# 调用时 **：把字典拆开，当关键字参数
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)            # 等价 parrot(voltage=..., state=..., action=...)
```

- 场景：数据存在列表/字典里，函数要求独立参数 → 拆包对接

### 4.9.6 Lambda 表达式（用完即弃的一次性函数）

**语法：`lambda 参数: 表达式`** —— 自动返回表达式结果，不用写 `return`；只能一个表达式（一行搞定的逻辑才用）

```python
add = lambda a, b: a + b     # 等价于 def add(a, b): return a + b
add(3, 5)                    # 8
```

- 语法糖：和常规函数定义完全等价，只是**不取名**
- 用途就两个：① 被返回（工厂造函数）② 被当参数塞给别人（排序裁判）

```python
# 用法一：工厂造函数（lambda 记住外面的 n —— 闭包雏形）
def make_incrementor(n):
    return lambda x: x + n

add42 = make_incrementor(42)   # 出厂一台"加42"的机器
add42(0)                       # 42
add42(1)                       # 43

# 用法二：sort 的 key 裁判（指定排序看哪一项）
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])   # 只看单词字母序
# [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
pairs.sort()                           # 不写 key 则看数字 → 1,2,3,4
```

- 为什么用 lambda 不用 def：裁判函数只用一次、就一行、没起名的意义 → 原地写完原地用
- 不会替换 def：多行逻辑仍用 def，lambda 只是"顺手塞个小函数"的快捷方式

### 4.9.7 文档字符串（docstring 的格式约定）

写作规范（非语法强制，`help()` / IDE 悬浮提示按此展示）：

1. **第一行 = 一句话摘要**：大写开头、句点结尾；不写名字和类型（`help()` 本来就显示函数名）
2. **第二行 = 空行**：视觉上分隔摘要和细节
3. **后面随便写**：调用约定、副作用、注意事项……

```python
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything:

        >>> my_function()
        >>>
    """
    pass

print(my_function.__doc__)   # 输出时缩进被自动去除（对齐到摘要行）
```

- **缩进自动去除**：解析器会去掉公共前导空格，不用手动对齐
- `>>>` 是 doctest 格式：文档里的示例代码可以当测试跑（现在知道即可）
- 对比记忆：docstring = 运行时还在（`__doc__`/`help()`/悬浮提示），`#` 注释 = 运行前丢弃

### 4.9.8 函数注解（给参数贴类型标签）

```python
def f(ham: str, eggs: str = 'eggs') -> str:   # 参数后 : 类型，返回值前 -> 类型
    return ham + ' and ' + eggs

f.__annotations__
# {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
```

- **纯元数据，不影响运行**：Python 不检查类型，标了 str 传数字照跑（不是安检，是贴标签）
- 存进 `__annotations__` 字典：键 = 参数名 / 'return'，值 = 类型
- 价值：给人读签名 + IDE 悬停/补全提示 + mypy 等检查工具（PEP 484）
- 这里的 `str` 是类型标签（类），不是转换函数 `str()`

### 4.10 编码风格（PEP 8 核心 8 条）

代码是写给人读的，风格让"人读"容易：

1. 缩进 4 空格，不用 Tab
2. 一行 ≤ 79 字符
3. 空行分隔函数/类、函数内大代码块
4. 注释单独一行
5. 用 docstring
6. 运算符前后、逗号后空格，括号内不空格：`a = f(1, 2) + g(3, 4)`
7. 命名：类 `UpperCamelCase`，函数/变量 `lowercase_with_underscores`
8. UTF-8 编码，标识符不用非 ASCII 字符

```python
class ForestCarbonCalculator:      # 类：单词连写、首字母大写
    def compute_carbon(self):      # 函数/方法：小写 + 下划线
        pass
```

### 第 4 章小结（函数章知识框架）

```
4.8 定义函数（骨架）
├── 定义 vs 调用（菜谱 vs 做菜）★
├── return（递出不显示；不写 return 返回 None）★
├── 参数传递（按值传引用：不可变只换指向 / 可变穿透）★
├── 作用域（局部→全局→内置，从里往外找）★
├── 函数是对象（f = fib，比 C++ 函数指针更强）★
├── docstring（说明书）
└── PEP 8 命名

4.9 参数传法全谱 ★★（本章灵魂）
├── 4.9.1 默认参数（必选在前；可变默认值坑 → None）★
├── 4.9.2 关键字参数（位置在前；撞名报错）★
├── 4.9.3 / 和 *（斜杠左只排队，星号右只点名）○
├── 4.9.4 *args/**kwargs（打包收集，类 C++ 可变参数）★
├── 4.9.5 解包 *列表/**字典（调用时拆开，方向相反）★
├── 4.9.6 lambda（一次性函数，同 C++11 lambda）★
├── 4.9.7 docstring 格式 ○
└── 4.9.8 注解（贴标签，不影响运行）○

4.10 PEP 8 编码风格
```

★ = 必须练熟，○ = 知道即可

**量化相关 💰**：
- 函数是对象 → 策略 = 把策略函数交给回测框架（"给我一个函数"）
- 默认参数 + 关键字参数 → 策略参数配置（窗口、阈值），改参数不改代码
- `*args`/`**kwargs` → 包装/转发：统一接口收信号再分发
- 解包 `**字典` → 参数从配置文件读进来，`strategy(**config)` 一把拆开
- lambda + sort key → 按因子/收益率/相关性排序股票（排序场景之王）


