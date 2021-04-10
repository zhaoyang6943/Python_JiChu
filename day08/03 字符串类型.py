# 1. 作用
# 记录描述状态的作用

# 2. 定义
# msg = 'hello'  # msg = str('hello')

# 3. 类型转换
# str 可以把任意其他类型都转成字符串
# res = str({'k1':123})
# print(res,type(res))

# 4. 使用

# 4.1 优先掌握

# 4.1.1 按索引取值（正向取+反向取）：只能取
# msg = 'hello world'
# 正向取
# print(msg[0])
# print(msg[5])
# # 反向取
# print(msg[-1])
# # 只能取，不能改！
# msg[0] = 'H'  # 会报错~


# 4.1.2 切片：索引的扩展应用，从一个大字符串中拷贝出一个子字符串（顾头不够尾，步长）
# 顾头不顾尾
# msg = 'hello world'
# res = msg[0:5]  # 取值
# print(res)

# 步长
# msg = 'hello world'
# res = msg[0:5:2]  # 取值后，步长2，意味着每两个字符取一个值
# print(res)

# 反向步长
# msg = 'hello world'
# res = msg[5:0:-1]  # 反向步长，从第五个，向第一个迈步
# print(res)

# 默认情况下
# msg = 'hello world'
# res = msg[0:15]
# # res = msg[:]  # 等同于上面
# print(res)

# 倒着写
# msg = 'hello world'
# res = msg[::-1]  # 将整个字符串倒着写，原字符串没有变化，只是拷贝一个新的。
# print(res)

# 4.1.3 长度 len

# msg = 'hello world'
# print(len(msg))


# 4.1.4 成员运算in和not in
# 判断一个字符串是否存在于一个大字符串中
# print("alex" in 'alex is sb')
# print(not 'alex' in 'alex is sb')  # 不推荐使用,阅读不友好
# print('alex' not in 'alex is sb')  # 等同于上面


# 4.1.5 移除字符串左右两侧的符号strip
# 默认去掉的是空格
# msg = '    yang    '
# res = msg.strip()
#
# print(msg)  # 不会改变原值，字符串是不可变类型
# print(res)  # 是产生了新增

# 默认去掉的是空格
# msg = '****yang****'
# res = msg.strip('*')
#
# print(msg)  # 不会改变原值，字符串是不可变类型
# print(res)  # 是产生了新增

# 了解：strip只取两边，不去中间
# msg = '****y****ang**************'
# res = msg.strip('*')
#
# print(msg)  # 不会改变原值，字符串是不可变类型
# print(res)  # 是产生了新增


# msg = '**/*=-yang**-=()**'
# res = msg.strip('*/-=()')  # 移除括号里面的参数
# print(res)


# 应用，防止沙雕用户
# inp_user = input('your name:').strip()  # 用户在输入过程中，手抖动，在前面输入了空格，输入内容成为了“ egon”，可能会导致易用性不好
# inp_pwd = input('your pwd:').strip()
#
# if inp_user == 'egon' and inp_pwd == '123':
#     print('登陆成功')
# else:
#     print('账户名密码错误')


# 4.1.6 切分split，是索引的扩展应用。
# 把一个字符串按照某种分隔符进行切分，得到一个列表！
# info = 'yang 18 male'
# res = info.split()  # 两个参数，默认空格分割
# print(res)

# 指定分隔符
# info = 'yang:18:male'
# res = info.split(':')  # 两个参数，默认空格分割
# print(res)

# 指定分隔次数(了解，通常没啥用)
# info = 'yang:18:male'
# res = info.split(':',1)  # 两个参数，默认空格分割
# print(res)  # ['yang', '18:male']


# 4.1.7 循环

# info = 'yang:18:male'
# for i in info:
#     print(i)



# 4.2 需要掌握

# 4.2.1 strip，lstrip，rstrip  # 移除左边，移除右边
# msg = '****yang****'
# print(msg.strip('*'))
# print(msg.lstrip('*'))  # 移除左边
# print(msg.rstrip('*'))  # 移除右边


# 4.2.2 lower，upper  # 大写，小写转换
# msg = 'ASFsdfwertyuiDFGTHJK'

# print(msg.lower())
# print(msg.upper())


# 4.2.3 startswith，endswith，判断正确，返回True和False
# print("alex is sb".startswith("alex"))
# print("alex is sb".endswith("sb"))


# 4.2.4 split,rsplit：将字符串切成列表
# info = "yang:18:male"
# print(info.split(":",1))  # ['yang', '18:male']
# print(info.rsplit(":",1))  # ['yang:18', 'male']
# print(info.rsplit(":"))  # ['yang', '18', 'male']


# 4.2.5 join：把列表拼接成字符串！！
# l = ['yang', '18', 'male']
# res = l[0] +":" +l[1]+"+" + l[2]

# res = ":".join(l)  # 按照某个分隔符号，把元素全为字符串的列表拼接成一个大字符串
# print(res)

# l1 = [1,"2","3"]
# res1 = "".join(l1)  # 注意列表中不能是非字符串的元素
# print(res1)

# 4.2.6 replace，替换，默认替换字符串全部符合的信息
# msg = "you can you up no can no bb"
# print(msg.replace("you","YOU"))  # 默认替换全部的you
# print(msg.replace("you","YOU",1))  # 替换后面加上数字，表示替换的次数


# 4.2.7 isdigit
# 判断字符串是否由数字组成
# print("123".isdigit())
# print("123.1".isdigit())

# 应用，之前为了防止用户手抖，用了移除空格的方法，strip。现在为了防止用户在输入数字密码时，输入其他的类型信息，
# 就可以用isdigit来先判断输入的字符串是不是数字

# age = input("请输入你的年龄：").strip()
# if age.isdigit():
#     age = int(age)  # 转换类型
#     if age>18:
#         print("猜大了")
#     elif age<18:
#         print("猜小了")
#     else:
#         print("猜对了")
#
# else:
#     print("请输入数字！")



# 4.3 了解

# 4.3.1 find，rfind，index，rindex，count
# msg = "hello yang hahahaha"

# 找到返回起始索引
# print(msg.find("e"))  # 返回要查找的字符串在大字符串中的起始索引
# print(msg.find("yang"))
# print(msg.index("e"))
# print(msg.index("yang"))

# 找不到
# print(msg.find("tang"))  # 找不到信息时，会返回  “-1”。
# print(msg.index("123"))  # 找不到信息时，会直接报错！抛出异常

# count 在字符串中出现多少次
# msg = "yang ooo uuu 123 qwe ooo yang 123 , , !!"
# print(msg.count("yang"))


# 4.3.2 center，ljust，rjust，zfill
# print("egon".center(50,'*'))  # 一个字符串，以egon为中心要足够50个字符，如果不够的话，要“*”填充
#
# print("egon".ljust(50,'*'))  # 左对齐
#
# print("egon".rjust(50,'*'))  # 右对齐
#
# print("egon".zfill(50))  # 默认用 “0” 填充，默认右对齐


# 4.3.3 expandtabs
# msg = 'hello\tworld'
#
# print(msg.expandtabs(1))  # 设置制表符代表的空格数1


# 4.3.4 capitalize，swapcase，title
# print("hello world yang 啊".capitalize())  # 首字母大写
# print("hello world yang 啊".swapcase())  # 大小写字母反转，小写变大写，大写变小写
# print("hello world yang 啊".title())  # 将每个字母字符串的开头变为大写


# 4.3.5 is 系列
# print('abc,样 y'.islower())  # 判断字符串是否小写
# print('ABC，样 y'.isupper())  # 判断字符串是否大写
# print('abc'.isdigit())  # 判断字符串是否数字
# print('Abc样 U'.istitle())  # 判断字符串中的每个单词是否首字母大写
#
# print("="*100)
# print('abcAbc样 U123'.isalnum())  # 判断字符串必须是字母或数字组成
# print('abcAbc样 U'.isalpha())  # 判断字符串必须由字母组成
# print('abc'.isspace())  # 判断字符串由空格组成
# print('abc'.isidentifier())  # 判断字符串中字母数字下划线组成，关键字；判断标识符是不是合法的


# 4.3.6 is 数字系列
num1 = b'4'  # bytes
num2 = u'4'  # unicode,python3中无需加u就是unicode
num3 = '四'  # 中文数字
num4 = 'Ⅳ'  # 罗马数字

# isdigit只能识别：num1 ，num2
# print(num1.isdigit())
# print(num2.isdigit())
# print(num3.isdigit())
# print(num4.isdigit())


# isnumeric 可以识别：num2 ， num3 ， num4    # 跟银行有关的，判断数字时，就可以用这个  “isnumeric”
# print(num2.isnumeric())
# print(num3.isnumeric())
# print(num4.isnumeric())


# isdecimal 只能识别：num2
print(num2.isdecimal())
print(num3.isdecimal())
print(num4.isdecimal())


"""
总结：
1. 能存几个值？（数字类型和字符串类型）
    都是一个

2. 有序还是无序（数字类型和字符串类型）
    有序还是无序，看是否有索引
    整型没有序
    浮点型没有序
    字符串被归类有序类型

3. 可变还是不可变（数字类型和字符串类型）
    都是不可变类型

"""

'''
强烈推荐：电影====》    《爆裂鼓手》
'''