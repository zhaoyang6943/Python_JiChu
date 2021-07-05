# 是什么，为什么要有，如何用

# 重复做某事，atm，重复输入密码

'''
while 条件：
    代码块

'''
# 1. while 循环，又叫做条件循环
# count = 0
# while count<10:
#     print(count)
#     count+=1
#
# print(123)

# 2. 死循环与效率问题

# while True:
#     name=input("请输入信息：")
#     print(name)

#
# while True:
#     1+1

# 纯计算，无IO的死循环导致致命的效率问题

# while 1:
#     print("123")

# 3. 循环的应用

# 两个问题：1. 重复代码  2. 输入对了怎么做？

# while 1:
#     name = input("请输入您的名字：")
#     pwd = input("请输入您的密码：")
#     if name == 'yang' and pwd == '123':
#         print('登录成功')
#     else:
#         print("账户名或密码错误")


# 4. 退出循环的两种方式
# 方式一：将条件改为False

# tag = True
# while tag:
#     tag = False
#     name = input("请输入您的名字：")
#     pwd = input("请输入您的密码：")
#     if name == 'yang' and pwd == '123':
#         print('登录成功')
#     else:
#         print("账户名或密码错误")

# tag = True
# while tag:
#
#     name = input("请输入您的名字：")
#     pwd = input("请输入您的密码：")
#     if name == 'yang' and pwd == '123':
#         print('登录成功')
#         tag = False  # 之后的代码还会运行，下次循环判断条件时才生效
#     else:
#         print("账户名或密码错误")
#
#     print("====end====")


# 方式二：break，只要运行到break就会立刻终止本层循环

# while True:
#     name = input("请输入账户名：")
#     pwd = input("请输入密码：")
#     if name == 'yang' and pwd == '123':
#         print('success')
#         break  # 立刻终止本层循环
#     else:
#         print("账户名或密码错误。")
#
#     print('='*10 + "end" + '='*10)


# 5. while循环嵌套

# while 循环嵌套与结束案例一：

# while True:
#     name = input("请输入账户：")
#     pwd = input("请输入密码：")
#
#     if name == 'yang' and pwd == '123':
#         print('登录成功。')
#         while True:
#             cmd = input("请输入指令：")
#             print("指令{x}正在运行".format(x=cmd))
#             if cmd == "q":
#                 print("退出成功")
#
#                 break
#
#         break
#     else:
#         print('账户名或密码错误')


# 改变条件的方式，tag
# tag = True
# while tag:
#     name = input('请输入账号')
#     pwd = input('请输入密码')
#     if name == 'yang' and pwd =='123':
#         print('登录成功')
#         while tag:
#             cmd = input("请输入指令")
#             if cmd == 'q':
#                 tag = False
#             else:
#                 print('命令{x}正在运行'.format(x=cmd))
#
#     else:
#         print('账户名或密码错误')


# 6. while + continue ：结束本次循环，直接进入下一次
# 强调：在continue之后添加同级代码毫无意义，因为永远无法执行
# 需求：当打印4的时候，跳过

# count = 0
# while count< 6:
#     if count == 4:
#         count+=1
#         continue  # 结束本次循环，直接进入下一次
#
#     print(count)
#     count+=1


# 7. while + else： 专门针对break！如果while循环，没有被break干死，那么就会执行else
# 需求：当ATM机输入错误三次，直接结束循环；ATM登录成功后，输入q，直接退出操作。

count = 0
while count < 3:
    name = input("请输入账号：")
    pwd = input("请输入密码：")

    if name == 'yang' and pwd == '123':
        print("登录成功")
        while True:
            cmd = input("请输入指令：")
            if cmd == 'q':
                break  # 退出当前循环，但是退出当前循环后，整体的大的循环在会运行三遍，需要在退出大循环
            else:
                print("命名{x}正在运行".format(x=cmd))

        break  # 当输入指令q后，会依旧要执行三遍。所以添加这边登录成功的break，直接退出整个循环

        print("用户或账户名错误")
        count += 1

else:
    print("输入错误三次，已退出！")
