
# fibo.py v2 —— 我的第一个模块：斐波那契工具箱
print('fibo 模块被加载了！当前名牌:', __name__)      # 观察：只初始化一次

answer = 42                      # 模块级变量（fibo 家的私有财产）

def fib(n):
    """打印到 n 为止的斐波那契数列"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

def fib2(n):
    """返回到 n 为止的斐波那契数列（列表）"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
