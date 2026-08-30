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

例子的格式约定（章首说明，读教程必备）

| 例子里 | 含义 |
|---|---|
| `>>>` 开头的行 | **你自己敲**的内容（只敲提示符后面的部分） |
| 没有提示符的行 | **电脑的输出**，不用敲 |
| 多行语句末尾的空行 | 敲一个空回车表示"语句结束" |

提示：网页右上角点 `>>>` 可以隐藏提示符，方便把输入行整段复制到自己终端。

> 对笔记的意义：在 VS Code 里写 .py 文件没有提示符这回事，这条主要用来**读教程时别把输出行也抄进代码**。

注释

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



### 3.1. Python 用作计算器

#### 3.1.1. 数字

- 整数（如，`2`、`4`、`20` ）的类型是 [`int`](https://docs.python.org/zh-cn/3.10/library/functions.html#int)，带小数（如，`5.0`、`1.6` ）的类型是 [`float`]

- 除法运算 (`/`) 总是返回浮点数



```python
print(17//3) #如果要做 [floor division](https://docs.python.org/zh-cn/3.10/glossary.html#term-floor-division) 得到一个整数结果你可以使用 `//` 运算符

17 % 3 #余数运算符 %
5**2 #乘方运算符
width = 20 #赋值    变量必须赋值 否则报错
```

- Python 全面支持浮点数；混合类型运算数的运算会把整数转换为浮点数：

```
>>> 4 * 3.75 - 1
14.0
```

#### 3.1.2. 字符串

斜杠

- 用单引号（`'……'`）或双引号（`"……"`）标注的结果相同

- 反斜杠 `\` 用于转义：

- 如果不希望前置 `\` 的字符转义成特殊字符，可以使用 *原始字符串*，在引号前添加 `r` 即可：

字符串合并

- 字符串可以用 `+` 合并（粘到一起），也可以用 `*` 重复

- 合并多个变量，或合并变量与字面值，要用 `+`：

- ```
  >>> prefix = 'Py'
  >>> prefix + 'thon'
  'Python'
  ```



索引

- [immutable](https://docs.python.org/zh-cn/3.10/glossary.html#term-immutable) 字符串

- 字符串支持 *索引* （下标访问），第一个字符的索引是 0。单字符没有专用的类型，就是长度为一的字符串：
- 索引还支持负数，用负数索引时，从右边开始计数：

```
>>> word[-1]  # last character
'n'
>>> word[-2]  # second-last character
'o'
>>> word[-6]
'P'
```



切片，索引指向的是字符 *之间* ，第一个字符的左侧标为 0，最后一个字符的右侧标为 *n* ，*n* 是字符串长度。例如：

```
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```





#### 3.1.3. 列表

Python 支持多种 *复合* 数据类型，可将不同值组合在一起。最常用的 *列表* ，是用方括号标注，逗号分隔的一组值。*列表* 可以包含不同类型的元素，但一般情况下，各个元素的类型相同：

 [mutable](https://docs.python.org/zh-cn/3.10/glossary.html#term-mutable) 类型

（1）方括号

```
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
```

（2）索引和切片：

```
>>> squares[0]  # indexing returns the item
1
>>> squares[-1]
25
>>> squares[-3:]  # slicing returns a new list
[9, 16, 25]
```

（3）+ 加号可以合并

（4）`append()` *方法* 可以在列表末尾添加新元素

（5）嵌套列表

```
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
```

### 3.2. 走向编程的第一步

## 4.更多控制流工具

除了上一章介绍的 [`while`](https://docs.python.org/zh-cn/3.10/reference/compound_stmts.html#while) 语句，Python 还支持其他语言中常见的流程控制语句，只是稍有不同。

### 4.1. `if` 语句

```
x= int(input("please enter an integer:"))
if x<0:
    x=0
    print('Negative changed to zero')
elif x==0:
    print('Zero')
elif x==1:
    print('Single')
else:
    print('More')
```

### 4.2. `for` 语句

```python

```

for迭代

words=['林业','遥感','碳汇']

for w in words:

    print(w,len(w))

  

#删掉之后不会空着

words=['林业','遥感','碳汇']

for w in words:

    if w!='林业':

        words.remove(w)

print(words)

#['林业', '碳汇']

  


#复制快照

words=['林业','遥感','碳汇']

for w in words.copy():

    if w!='林业':

        words.remove(w)

#['林业']

  


#反向，符合的抓进去

words=['林业','遥感','碳汇']

forest_words = []

for w in words:

    if w== '林业':

        forest_words.append(w)

print(forest_words)
print(words)```


### 4.3 range()函数

内置函数 range()用于生成等差数列：

```
for i in range(5):
    print(i)

0
1
2
3
4
```



生成的序列绝不会包括给定的终止值；

```
list(range(5, 10))
[5, 6, 7, 8, 9]

list(range(0, 10, 3))
[0, 3, 6, 9]

list(range(-10, -100, -30))
[-10, -40, -70]


```

要按索引迭代序列，可以组合使用 [`range()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#range "range") 和 [`len()`](https://docs.python.org/zh-cn/3/library/functions.html#len "len")：

```
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

0 Mary
1 had
2 a
3 little
4 lamb


```



range()不等同于列表

```python
(range(10))
print(list(range(10)))
```

### 4.4. `break` 和 `continue` 语句

```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break

4 equals 2 * 2
6 equals 2 * 3
8 equals 2 * 4
9 equals 3 * 3
```

[`continue`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#continue) 语句将继续执行循环的下一次迭代

```python
for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")

Found an even number 2
Found an odd number 3
Found an even number 4
Found an odd number 5
Found an even number 6
Found an odd number 7
Found an even number 8
Found an odd number 9
```



