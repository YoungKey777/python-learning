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


