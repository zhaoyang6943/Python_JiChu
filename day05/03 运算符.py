# 学习的思路：什么是？为什么要有这个？

# 1. 算术运算符
# print(111 + 3)
# print(type(100 - 3.1))
#
# print(10 / 3)  # 带小数
# print(10 // 3)  # 只保留整数部分
#
# print(10 % 3)  # 取余
#
# print(10 ** 3)  # 代表10的3次方

# 2. 比较运算符
# print(1 > 3)
#
# print(1 == 1)
#
# print(10 >= 10)
# print(10 <= 3)

# name=input('your name')
# print('agen' == name)

# 3. 赋值运算符


# 3.1 增量赋值


# age = 18
# age += 1  # age = age +1
# print(age)
# age-=1
# age*=3
# age/=2
# age**=3

# 3.2 链式赋值

# x=10
# y=x
# z=y
z=y=x=10  #  链式赋值
print(x,y,z)
print(id(x),id(y),id(z))

# 3.3 交叉赋值
m=10
n=20
# 交叉值
# temp =m
# m=n
# n=temp

m,n=n,m  # 一行代码搞定多行代码
print(m ,n)

# 3.4 解压赋值
salaries=[111,222,333,444,555]  # 解压缩
# mon1=salaries[0]
# mon2=salaries[1]
# mon3=salaries[2]
# mon4=salaries[3]
# mon5=salaries[4]

# 解压赋值
mon1,mon2,mon3,mon4,mon5=salaries  # 对应的变量名少一个不行，多一个不行！

print(mon1)
print(mon2)
print(mon3)
print(mon4)
print(mon5)

# 需求：一个列表中有30个值，但是想要取出前3个值，怎么做？
x,y,z,*_=salaries  # *_,剩下的所有的。（ps：“_”变量名不要用下划线，代表一般是废弃的变量）
print(x,y,z)
print(_)

# 需求：取后三个值？
*_,x,y,z=salaries

# 需求，取中间的呢？-------不行~

# 需求，可以取两头的值，不能取中间的值。
x,*_,y,z=salaries
print(x,_,y,z)

# 需求，解压字典呢？
d={"a":123,"b":456,"c":789,"d":"abc","e":"edf"}

x,y,z,*_=d  # 解压出来的是字典的key值
print(x,y,z,_)
