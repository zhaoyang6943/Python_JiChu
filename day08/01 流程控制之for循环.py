# 商人的地位上来后，世风日下，商人重利轻离别

'''
1. 什么是for循环？
    循环就是重复做某件事，for循环是python提供第二种循环机制

2. 为什么要有for循环
    理论上for循环能做的事情，while循环都可以做，之所以要有for循环，一定是for循环在做某种场景下有独到之处。
    for循环在循环取值上比while循环更便利。（遍历）

3. 如何用for循环
    语法：
    for 变量名 in 可迭代对象：  # 可迭代对象可以是：列表、字典、字符串、元祖、集合。。。
        代码块

'''

# 一、基本使用之循环取值

# 案例1：循环取值
# 简单版
# for i in ['yang','zhao','zhu']:
#     print(i)

# 复杂版
# l = ['yang','zhao','zhu']
# i = 0
# while i<3:
#     print(l[i])
#     i+=1


# 案例2：字典循环取值
# 简单版
dic = {'k1':'111','k2':'222','k3':'333'}
for k in dic:
    print(k,dic[k])

# 复杂版：while循环可以便利字典，太麻烦了

# 案例3：字符串循环取值
# 简单版
# msg = 'you can you up,no can no bb'
# for x in msg:
#     print(x)

# 复杂版：。。。。

# 二：总结for循环与while循环的异同

# 1. 相同之处：都是循环，for循环可以干的事，while循环也可以干
# 2. 不同之处：
#         while循环称之为条件循环，循环次数取决于条件何时变为假
#         for循环称之为“取值循环”。。。循环次数取决于in后包含的值的个数
# for x in [1,2,3]:
#     print("====>")
#     print("8888")

# 三：for循环控制循环次数：range
# 有局限性
# for i in 'abc':
#     input_name = input("please input your name:")
#     input_pwd = input("please input your password:")

# 思考：总不能循环一千次，一万次时，我abc写一千次一万次吧！

# range 功能介绍
key = {"aa":"123"}
for k in key:
    print(k,key[k])

'''
>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(1,9)  # 1.。。。8
[1, 2, 3, 4, 5, 6, 7, 8]
>>> range(1,9,1)
[1, 2, 3, 4, 5, 6, 7, 8]
>>> range(1,9,2)
[1, 3, 5, 7]
>>>
'''

# for i in range(30):
#     print("====>")


# for + break:同while循环一样
# for + else：同while循环一样

# for i in range(3):
#     name = input("请输入账号：")
#     pwd = input("请输入密码：")
#
#     if name == 'yang' and pwd == '123':
#         print("登录成功")
#         while True:
#             cmd = input("请输入指令：")
#             if cmd == 'q':
#                 break  # 退出当前循环，但是退出当前循环后，整体的大的循环在会运行三遍，需要在退出大循环
#             else:
#                 print("命名{x}正在运行".format(x=cmd))
#
#         break  # 当输入指令q后，会依旧要执行三遍。所以添加这边登录成功的break，直接退出整个循环
#     else:
#         print("用户或账户名错误")
#
#
# else:
#     print("输入错误三次，已退出！")


# 卡耐基：人性的弱点
# 提高情商

# 四。 range的补充,（了解）
# 1. for搭配range，可以按照索引取值，但是麻烦，所以不推荐
#
# l=['123','456','789']
# for i in range(len(l)):
#     print(i,l[i])
#
# for i in l:
#     print(i)

# 2. range()在python3里得到的是一只“会下蛋的老母鸡”，
# 在python2中，就是一筐的鸡蛋


# 五：for + continue

# for i in range(6):
#     if i == 4:continue  # 可以写到一行。。但是规范是写到下一行
#
#     print(i)

# 六：for循环嵌套：外层循环循环一次，内层循环需要完整的循环完毕

# for i in range(3):
#     print("外层循环=========》")
#     for j in range(5):
#         print("内层循环===》")

# 补充：终止for循环只有break一种方案


# 补充，print的用法
# print('hello','world','yang')  # ','逗号代表着空格
# print('hello%s,world%s'%('123','qwe'))  # 这是人家字符串的用法，不是print
# print('hello\n')  # 换行符
# print('world')  # print的默认换行
#
# print('hello\n',end='')  # 字符串用自己的换行符，不用默认print的
#
# print('hello',end='*')  # print将换行符改为“*”
# print('world',end='*')
