# demo.py —— 双身份演示
print('① 顶层：不管怎么启动都执行（函数定义都在这层）')

def 策略函数():
    return '🚀 买入信号'

print('② 顶层又执行了：我在 if 外面')

if __name__ == '__main__':
    print('③ 我是主角！直接运行才进来')
    print('   测试一下:', 策略函数())
else:
    print('③ 我是工具！我被 import 了，主角分支没执行')