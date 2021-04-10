# 一：int类型

# 1. 作用：
# 2. 定义：
# age = 10  # age = int(10)
# 名字(参数)
# print('hello world')

# int()
# print()
# input()
# 相当于工厂，有产品，有的没有产品（print没有产品）
# x = int(10)
# # name = input("xxx")
# res = print("123")
# print(res)  # 证明了print是貔貅，只吃不拉

# 3. 类型转换：
# res=int("1258752")  # 纯数字的字符串可以转换成整形
# print(res,type(res))

# 3.1 了解
# 10进制转成其他进制
# 10进制转2进制
# 除2取余，倒着写：10的二进制1011

# print(bin(11))  # 10进制转2进制0b1011
#
# print(oct(11))  # 10进制转8进制0o13
#
# print(hex(11))  # 10进制转16进制0xb

# 3.2 其他进制转10进制
#  2进制转10进制
# print(int('0b1011',2))
# #  8进制转10进制
# print(int('0o13',8))
# #  16进制转10进制
# print(int('0xb',16))

# 4. 使用：
# 内置方法：
# 无


# 二：float类型


# 1. 作用：
# 2. 定义：
salary = 3.1  # salary = float(3.1)

# 3. 类型转换：
res = float("3.11")  # 字符串转为浮点类型
print(res,type(res))

# 4. 使用：
# int与float没有需要掌握的内置方法
# 他们的使用就是数学运算+比较运算