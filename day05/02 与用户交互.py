# 1. 如何接收用户的输入
# 基础阶段，写程序的思路；
# 把自己想象成一台计算机

# 在python3中，input会将用户输入的所有内容，都存成字符串内容
# username = input("请输入您的账号：")
# print(username,type(username))


# age = input("请输入您的年龄：")
# print(age,type(age))
#
# age = int(age)
# print(age>16)


# python2中输入什么就是什么类型（了解）

# 思考？是否python2会比python3，更加方便呢？
# 答案：并不是，python2会要求用户必须输入某个类型的值。。。


# 2. 字符串的格式化输出

# 2.1 %   元老级别的格式化输出（速度最慢）
# 值按照位置与%s一一对应，少一个不行，多一个也不行
res = "my name is %s ,my age is %s" % ('egon', '18')
print(res)

# 以字典的形式传值，打破位置的限制
res1 = "my name is %(name)s ,my age is %(age)s" % {"name": 'egon', "age": '18'}
print(res1)

# %d只能接收int类型；%s可以接收任意形式的值
print('my age is %d'%18)

# 2.2 str.format 兼容性好，推荐使用（速度一般）

# 按照位置取值
res2="我的名字是{0}{1}，我的年龄是{1}{0}".format('yang',18)
print(res2)

res3="我的名字是{}，我的年龄是{}".format('yang',18)
print(res3)

# 打破位置的限制，按照key=value传值
res4="我的名字是{name}{age}，我的年龄是{age}".format(age=18,name='yang')
print(res4)
1
# 2.3 f  python3.5之后才支持的方式（速度最快）

x =input("your name:")
y = input("your age:")
res5=f'我的名字是{x}我的年龄是{y}'
print(res5)