'''
语法1：
if 条件：
    代码1
    代码2
    代码3


语法2：
if 条件:
    代码块
else:
    代码块


语法3：
if 条件：
    代码块
elif 条件：
    代码块
elif 条件：
    代码块
。。。

语法4：
if 条件：
    代码块
    if 条件：
        代码块

elif 条件：
    代码块
else：
    代码块


'''

# 语法1：
age = 50
gender = 'femal'
is_beautiful = True
star = '水瓶座'

# if age >16 and age < 20 and star == "水瓶座":
#     print("我喜欢，我们在一起吧！")


# print('其他代码。。。。。。。。。。。。。。')

# 语法2：
if age > 16 and age < 20 and star == "水瓶座":
    print("我喜欢，我们在一起吧！")
else:
    print("我逗你玩呢！")

# 语法3：
score = input("请输入您的分数：")
score = int(score)

if score >= 90:
    print("优秀")
elif score >= 80 and score < 90:
    print("良好")
elif score >= 70 and score < 80:
    print("普通")
elif score >= 60 and score < 70:
    print("及格")
else:
    print("不及格")

# 输入成绩，基本上不用后面的and条件
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 70:
    print("普通")
elif score >= 60:
    print("及格")
else:
    print("不及格")
