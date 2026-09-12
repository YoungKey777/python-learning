#print("hello python")


# print("hello")
# print(1 + 1)
# print("量化" + "学习")


#3.Python速览

# print(17//3) 
# print('py'*3)


# x= int(input("please enter an integer:"))
# if x<0:
#     x=0
#     print('Negative changed to zero')
# elif x==0:
#     print('Zero')
# elif x==1:
#     print('Single')
# else:
#     print('More')


# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w)



# # for迭代
# words=['林业','遥感','碳汇']
# for w in words:
#     print(w,len(w))

# #删掉之后不会空着
# words=['林业','遥感','碳汇']
# for w in words:
#     if w!='林业':
#         words.remove(w)
# print(words)
# #['林业', '碳汇']


# #复制快照
# words=['林业','遥感','碳汇']
# for w in words.copy():
#     if w!='林业':
#         words.remove(w)
# #['林业']


# #反向，符合的抓进去
# words=['林业','遥感','碳汇']
# forest_words = []
# for w in words:
#     if w== '林业':
#         forest_words.append(w)
# print(forest_words)
# print(words)


# for i in range(5):
#     print(i)


# (range(10))
# print(list(range(10))).

# for num in range(2, 10):
#     if num % 2 == 0:
#         print(f"Found an even number {num}")
#         continue
#     print(f"Found an odd number {num}")


# for num in range(1, 6):
#     print(f"—— 进入第 {num} 轮 ——")
#     if num == 3:
#         print("第 3 轮：走了 if 分支")
#     else:
#         print(f"第 {num} 轮：走了 else 分支")


# for num in range(1, 6):
#     print(f"—— 进入第 {num} 轮 ——")
#     if num == 3:
#         continue          # ← 注意这行
#     print(f"第 {num} 轮：continue 后面的代码执行了")



# def http_error(status):
#     match status:
#         case 400:
#             return "Bad request"
#         case 404:
#             return "Not found"
#         case 418:
#             return "I'm a teapot"
#         case _:
#             return "Something's wrong with the internet"
# print(http_error(111))   # ← 加这两行：调用函数 + 打印结果
# print(http_error(500))


# 4.7 match
# point=[3,5]
# match point:
#     case (0, 0):
#         print("Origin")
#     case (0, y):
#         print(f"Y={y}")
#     case (x, 0):
#         print(f"X={x}")
#     case (x, y):
#         print(f"X={x}, Y={y}")
#     case _:
#         raise ValueError("Not a point")

# 4.8定义函数
# def fib(n):
#     """Print a Fibonacci series less than n."""
#     a,b = 0,1
#     while a<n:
#         print(a,end='')
#         a,b = b, a+b
#         print()
# fib(2000)
        

# def add(a, b):
#     """计算 a 加 b，返回结果。"""
#     return a + b

# help(add)     # ← 终端会显示说明书


# def change_num(n):
#     n=100

# x=5
# change_num(x)
# print(x)

# def change_list(lst):
#     lst.append(99)

# my_list =[1,2,3]
# change_list(my_list)
# print(my_list)

# fruits = ['orange','apple', 'pear','banana','kiwi','apple','banana']
# print(fruits);
# print(fruits.count('apple'))  #数这个列表里有几个apple
# print(fruits.index('banana',4 ))# 4 号位开始查找下一个 banana
# fruits.reverse()#翻转列表
# print(fruits)
# fruits.append('grape')#在列表末尾添加一项
# print(fruits)
# fruits.sort()#原地排序列表中的元素 按照首字母的顺序
# print(fruits)
# print(fruits.pop())#跳出最后一个 返回的也是最后一个
# print(fruits)

# 5.1.2用列表实现队列
# from collections import deque
# queue=deque(["Eric","John","Michael"])
# queue.append("Terry")
# print(queue);
# queue.append("Graham")          # Graham 到了
# print(queue);
# queue.pop()
# print(queue);
# queue.popleft()
# print(queue);

# 5.1.3列表推导式
# squares = []
# for x in range(10):
#     squares.append(x**2)

# squares
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

# vec = [-4, -2, 0, 2, 4]
# print([x*2 for x in vec])
# print([x*2 for x in vec if x>=0])
# print([abs(x) for x in vec]) # 在每个元素上调用一个方法

# freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# print([weapon.strip() for weapon in freshfruit])

# 嵌套
# vec = [[1,2,3], [4,5,6], [7,8,9]]
# [num for elem in vec for num in elem]

#5.1.4. 嵌套的列表推导式
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
# print(matrix)

# [[row[i] for row in matrix] for i in range(4)]
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])

# transposed
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]




#5.3元组和序列
## ---------- 1. 数字四兄弟 ----------
# i=42
# f=3.14
# b=True
# print("int整除",17//5)
# print("float除法",17/5)
# print("bool",b+1)

#---------- 2. 字符串：不可变、有索引 ----------
# word = "Python"
# print(word[0],word[1],word[3])
# s= "hello"
# s_new=s.upper()
# print("原串",s,"新串",s_new)


# ---------- 3. 列表：可变、最常用 ----------
# prices= [100,102,101]
# prices.append(105)
# prices[0]=99
# print("列表被改了",prices)


# ---------- 4. 元组：不可变、异质记录 ----------
# t = 12345,54321,"hello!"
# print(t[0])
# print(t)

# u= t,(1,2,3,4,5)
# print(u)

# u=[1,2,3]
# v=u,[3,2,1]
# u[0:3]=[33,34,35]
# del u[0]
# del u[1]
# del u[0]
# print(v)

# t = (5)
# print(t)
# t2=(5,)
# print(t2)
# print(len(t2))

# x, y = 1, 2          # 其实是：先打包成 (1, 2)，再解包给 x, y
# print(x)
# print(y)
# print(x,y)

# x, y = y, x          # 右边先打包 (2, 1)，再解包 → 交换成功
# print("右边先打包 (2, 1)，再解包 → 交换成功")
# print(x)
# print(y)
# print(x,y)

# a = [1, 2]
# a += [3]
# print(a)

# t = (1, 2)
# u = t
# t += (3,)
# print(u)


# t = (1, (2, 3), (4, (5, 6)))
# print(t[1])       # 猜？
# print(t[2][1])    # 猜？
# print(len(t))     # 猜？—— 3 还是 6？

#x, y, z = 1, 2        # 左边 3 个坑，右边只有 2 个值 → 猜报什么？
#a, b = 1, 2, 3        # 左边 2 个坑，右边 3 个值 → 猜报什么？

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# print(a - b)    # 猜？  {1, 2}（a 独有）
# print(a | b)    # 猜？  {1, 2, 3, 4, 5, 6}（合并去重）
# print(a & b)    # 猜？  {3, 4}（共同）
# print(a ^ b)    # 猜？  {1, 2, 5, 6}（各边独有）


# ① 去重 + 无序 + 查得快
# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)                 # 顺序乱吗？重复还在吗？
# print('apple' in basket)      # True
# print(basket[0])              # 猜？→ 应该报错（集合没有索引）

# ② 朋友圈四运算（自己造两个集合验证）
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# print(a - b)    # 猜？  {1, 2}（a 独有）
# print(a | b)    # 猜？  {1, 2, 3, 4, 5, 6}（合并去重）
# print(a & b)    # 猜？  {3, 4}（共同）
# print(a ^ b)    # 猜？  {1, 2, 5, 6}（各边独有）

# ③ 三个坑
# s = {}
# print(type(s))        # dict 不是 set！（坑 2）
# s2 = set()
# print(type(s2))       # set ✅
# s3 = {[1, 2]}         # 报错！（列表不能进集合，坑 3）

# ④ 去重实战：模拟数据源重复
# 代码列表 = ['600519', '000001', '600519', '300750', '000001']
# print(len(代码列表))              # 5
# print(len(set(代码列表)))          # 3 —— 去重后



# tel = {'jack': 4098}
# print(tel['irv'])            # 报错？什么错？
# print(tel.get('irv'))        # 不报错？输出什么？
# print(tel.get('irv', 0))     # 输出什么？
# d={'rack':1048}
# print('rack' in d  )


# s1={1,2,3}
# s2=set([1,2,3])
# s3=set('abracadabra')
# empty=set()
# fake={}
# # print(s1)
# # print(s2)
# print(s3)

# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for a,b in knights.items():
#     print(a,b)

# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for i, v in enumerate(['tic', 'tac', 'toe']):
#     print(i,v)
#     print('华丽的分割线')

# names = ['茅台', '平安', '宁德']
# prices = [1500, 45, 250]

# print(zip(names, prices))
# # <zip object at ...> —— 惰性，是个"拉链机"，要用 list() 兑现或 for 拉

# print(list(zip(names, prices)))
# # [('茅台', 1500), ('平安', 45), ('宁德', 250)] ← 每对是一个元组！

# print(dict(zip(names, prices)))
# print(type(zip([1,2],[3,4])))

# def 喊话(msg):
#     print('执行了:', msg)
#     return True

# print('结果:', 喊话('A') and 喊话('B') and 喊话('C'))

# def 喊话2(msg,ok):
#     print('执行了:', msg)
#     return ok

# print('结果:', 喊话2('A',False) or 喊话2('B',False) or 喊话2('C',True))

# prices = [1500, 45, 250]
# if (n := len(prices)) > 2:
#     print(f'有 {n} 只票，超过了 2 只') 

# 6. 模块（import 的完整世界观——量化的入口章）

# import fibo
# fibo.fib(1000)
# print(fibo.__name__)

# fib= fibo.fib
# fib(500)
# print('fibo 模块被加载了！当前名牌:', __name__)

# import demo
# print(demo.path)
# import sys
# print(sys.path)


# import math, fibo
# print(math.__file__)     # D:\Users\27182\anaconda3\lib\math.py ← 标准库的家
# print(fibo.__file__)     # e:\OB\...\code\fibo.py ← 你自己的家（脚本目录）

# import sys, math, fibo

# print('math 是内置模块吗?', 'math' in sys.builtin_module_names)   # → True
# print('fibo 是内置模块吗?', 'fibo' in sys.builtin_module_names)   # → False

# print(fibo.__file__)       # 纯 Python 模块：有户口 ✅
# print(hasattr(math, '__file__'))   # → False：C 模块没户口
# # print(math.__file__)     # 别再问了，会报错（就是刚才那行）


#6.2
# import sys
# print('A跑完：脚本没有ps1，符合预期')

# 更新daily并且push点格子

#6.3
# import fibo
# print(dir(fibo))

# import sys
# 'path' in dir(sys)             # True（6.1 搜索路径）


# import fibo, sys, builtins

# print('① fibo 口袋:', dir(fibo))
# # → ['__name__', 'answer', 'fib', 'fib2']

# print('② sys 熟人:')
# print('   path:', 'path' in dir(sys))
# print('   ps1:', 'ps1' in dir(sys))
# print('   getrefcount:', 'getrefcount' in dir(sys))

# print('③ builtins 老熟人:')
# print('   print:', 'print' in dir(builtins))
# print('   TypeError:', 'TypeError' in dir(builtins))
# print('   zip:', 'zip' in dir(builtins))

# print('④ 自己的口袋 fibo 在不在:', 'fibo' in dir())




# a = [1, 2, 3]
# import fibo
# dir()                          # ['__builtins__', '__name__', 'a', 'fibo', ...]
# # 为什么 print/len/zip 不用 import？→ 住在 builtins 模块
# import builtins
# 'print' in dir(builtins)       # True
# 'TypeError' in dir(builtins)   # True（第5章踩的坑全在这）
# # Python 启动时自动把 builtins 全家塞进命名空间 = "内置"的定义


# import sound.effects.echo                # 全名引用：sound.effects.echo.函数()（太长）
# from sound.effects import echo           # 推荐：echo.函数()
# from sound.effects.echo import echofilter  # 函数直接可用：echofilter()



# ── 6.4 实验：三种导入姿势 ─────────────────────────────
# import sound.effects.echo               # 姿势1：全名
# print('--- 姿势1 跑完 ---')

# from sound.effects import echo          # 姿势2：推荐
# print('--- 姿势2 跑完 ---')

# from sound.effects.echo import echofilter  # 姿势3：直接拿函数
# print('--- 姿势3 跑完 ---')


# ── 6.4 实验：__all__ 控制 import * ────────────────────
# from sound import *        # sound/__init__.py 里 __all__ = ['formats', 'effects']
# print('effects' in dir())  # True  ← 名单里的，进来了
# print('echo' in dir())     # False ← 没在名单里，* 不倒子模块
# print('wavread' in dir())  # False ← 同上


# import sound.effects.echo     # 这次第一行会多出: >>> sound 包已加载（初始化执行一次）
# print('--- 姿势1 跑完 ---')

# from sound import *
# print('effects 在不在:', 'effects' in dir())   # True（__all__ 白名单放行）
# print('echo 在不在:', 'echo' in dir())         # False（没名单的不倒）

# while True print('Hello world')     ← 前面加个 # 就行


# ── 8.1 语法错误实验 ────────────────────────────
# 实验1: 缺冒号(取消注释 → 看箭头骗局 + 连坐 → 看完注释回去)
# while True print('Hello world')
# 实验2: 括号没合(取消注释 → 报错追到文件末尾 unexpected EOF)
# print('字符串没关
# 实验3: 配合实验1玩连坐——实验1取消注释时,这行会被连坐打印不出:

# print('✅ 语法绿灯 = 当前文件没有任何语法错误')

# print(10 * (1/0))
# print(4 + spam * 3)

# print(int('2') + 2)        # 4   ← 字符串转数字 → 真·加法
# print('2' + str(2))        # '22' ← 数字转字符串 → 拼接
# print(type(int('2') + 2))  # int  ← 加法结果是数字
# print(type('2' + str(2)))  # str  ← 拼接结果是字符串

# import builtins
# print('ZeroDivisionError' in dir(builtins))   # True
# print('TypeError' in dir(builtins))           # True

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break          # int() 成功才会走到这 → 退出循环
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")

# try:
#     f = open('myfile.txt')     # 可能抛出 OSError（文件不存在/权限）
#     i = int(f.readline())      # 可能抛出 ValueError（内容不是数字）
#     print(i)
# except OSError as err:         # 第一个匹配的执行，其他不执行
#     print("OS error:", err)
# except ValueError:
#     print("Could not convert data to an integer.")
# # 一条 try 挂多张网，从上往下第一个接住算数


# class B(Exception): pass       # 祖辈
# class C(B): pass               # 父辈
# class D(C): pass               # 子辈（也是 C 和 B 的子类）
# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D: print("D")       # 子类在前！
#     except C: print("C")
#     except B: print("B")


# raise ValueError(1)

# ── 实验 3：裸 raise——中间层留痕再上交 ─────────────────
# def 内层():
#     raise NameError('HiThere')   # 源头在这
# def 中间层():
#     try:
#         内层()
#     except NameError:
#         print('中间层:记录到日志,然后上交')
#         raise                     # 原样转抛!
# 中间层()


# try:
#     open('database.sqlite')
# except OSError:
#     raise RuntimeError('unable to handle error')

# try:
#     open('database.sqlite')
# except OSError:
#     print('第一层：接住了 FileNotFoundError，准备上报')
#     raise RuntimeError('unable to handle error')
# except RuntimeError:        # ← 猜：这张网接得住上面上报的吗？
#     print('第二层：接住了 RuntimeError')


# ── 实验 B：上报的异常，被外层接住 —— 这次安静了 ──────────
# try:
#     try:
#         open('database.sqlite')
#     except OSError:
#         print('里层：接住了，上报 RuntimeError')
#         raise RuntimeError('打包成业务错误')
# except RuntimeError as e:
#     print('外层接住了：', e)
#     print('（屏幕上没有一个 traceback —— 因为有人接了）')

# try:
#     try:
#         raise ValueError('里层出事')
#     except ValueError:
#         print('里层接住，上报')
#         raise TypeError('中层出事')
# except TypeError as e:
#     print('外层接住：', e)

# def func():
#     raise ConnectionError
# try:
#     func()
# except ConnectionError as exc:
#     raise RuntimeError('哎哟我去,失败了') from exc


# try:
#     open('database.sqlite')
# except OSError:
#     raise RuntimeError from None  




# ── 实验 1：最小自定义异常（8.3 的 B/C/D 正式版）──
# class 数据缺失Error(Exception):
#     pass
# try:
#     raise 数据缺失Error('2026-08-01 的行情是空的')
# except 数据缺失Error as e:
#     print('抓到：', type(e).__name__, '-', e)

# ── 实验 2：带属性的自定义异常（官方"只提供属性"的用法）──
# class 拉取失败Error(Exception):
#     def __init__(self, 代码, 原因):
#         self.代码 = 代码
#         self.原因 = 原因
# try:
#     raise 拉取失败Error('600519', '网络超时')
# except 拉取失败Error as e:
#     print(f'股票 {e.代码} 拉取失败，原因：{e.原因}')

# ── 实验 3：没血统的下场（8.4 规则复验）───────────
# class 野异常(Exception):          # ← 故意不挂靠 Exception
#     pass
# try:
#     raise 野异常()
# except Exception as e:
#     print('接住了：', type(e).__name__, '-', e)
# 预期：接住了： TypeError - exceptions must derive from BaseException
# （raise 发现它没血统，当场换成 TypeError 抛出；这个 TypeError 又被你的网接住了）


#8.7
# ── 实验 1：连中断也要先收尾（官方例子）──────────
# try:
#     raise KeyboardInterrupt
# finally:
#     print('Goodbye, world!')
# 预期：先打印 Goodbye, world! → 再出现 traceback（收尾完才上报）

# def 吃掉异常():
#     try:
#         raise ValueError('本该抛出来')
#     finally:
#         return '我被返回值顶替了'
# print(吃掉异常())

#7.1
# import sys
# sys.stdout.write('write → ')
# sys.stdout.write('A')
# sys.stdout.write(' B\n')
# print('   ← 看，AB 黏在一起了，换行得自己补')
# try:
#     sys.stdout.write(123)
# except TypeError as e:
#     print('write(123) →', type(e).__name__, ':', e)
#     print('print(123) →', 123, '  ← 对比：print 自动把数字转成了字符串')

# import sys
# print(f'喂给 print → {0.4967:.2%}',' {0.4967:.2%}')
# sys.stdout.write(f'喂给 write → {0.4967:.2%}\n')   # 注意自己补的 \n
# print()

# ── 实验 1：str() vs repr() —— 亲眼对比 ──
# s = 'Hello, world.\n'
# print('str  →', str(s))
# print('repr →', repr(s))
# print('直接 print 字符串 →', s)


# s = 'Hello, world.\n'
# print('str  →', str(s), end='|')    # end='|' 把 print 那个自动换行换成竖线
# print('repr →', repr(s), end='|')
# print('直接 →', s, end='|')


# hello = 'hello, world\n'
# print('print(hello)  →')        # 真的换一行
# print(hello)
# print('print(repr(hello)) →', repr(hello))   # \n 现形
# 带空格的 = '  茅台  '
# print('看不出问题:', 带空格的, '| repr 一览无余:', repr(带空格的))

# ── 实验 3：format 和 f-string 是同一套格式规格，两种写法 ──
# yes_votes = 42_572_654
# total_votes = 85_705_149
# percentage = yes_votes / total_votes
# print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))   # 老写法
# print(f'{yes_votes:-9} YES votes  {percentage:2.2%}')  


# bugs = 'roaches'
# count = 13
# print('② 自说明   :', f'{bugs=} {count=}')
# print('② 自说明   :', f'{bugs} {count}')
# print('   等价写法:', f'bugs={bugs!r} count={count!r}')

# print(repr('3.14'.zfill(5)))

# 7.2 读写文件（`open` = 借书，`close` = 还书，`with` = 自动还）
# with open('demo.txt', 'w', encoding='utf-8') as f:
#     f.write('第一行\n第二行\n')
# print('刚写完 →', repr(open('demo.txt', encoding='utf-8').read()))


with open('demo.txt', 'a', encoding='utf-8') as f:      # 'a' 追加
    f.write('第三行\n')
print("用 'a' 之后 →", repr(open('demo.txt', encoding='utf-8').read()))