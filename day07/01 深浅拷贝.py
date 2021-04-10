
# pycharm中四个空格等于一个Tab键

list1=[
    'egon',
    'lxx',
    [1,2]
]

# 1. 二者分隔不开，list1改，list2也会跟着改，因为指向的就是同一个内存地址
# list2=list1
#
# list1[0]='EGON'
# print(list2)
#
# print(id(list1))
# print(id(list2))


# 2. 需求：
#   1. 拷贝一下原列表产生一个新的列表
#   2. 想让两个列表完全独立开，针对的是改操作的独立而不是读操作

# 3. 如何copy列表
# 3.1 浅拷贝copy

list3=list1.copy()
print(list3)

print("浅拷贝后列表id：")
print(id(list1))
print(id(list3))

print("浅拷贝后，列表中值的id：")
print(id(list1[0]),id(list1[1]),id(list1[2]))
print(id(list3[0]),id(list3[1]),id(list3[2]))

list1[0]='EGON'
list1[1]='LXX'
list1[2][0]=111
list1[2][1]=222

print("修改值后，列表信息展示：")
print(list1)
print(list3)

print("修改值后浅拷贝后列表id============：")
print(id(list1))
print(id(list3))

print("修改值后，列表中值的id变化：")
print(id(list1[0]),id(list1[1]),id(list1[2]))
print(id(list3[0]),id(list3[1]),id(list3[2]))

'''
小结：如果copy的是不可变类型（int、float、str、bool），那么就会全部copy；
但是如果copy的是可变类型（列表、字典），那么就不会copy
'''

list1=[
    'egon',
    'lxx',
    [1,2]
]

# 3.2 深拷贝
import copy

list4=copy.deepcopy(list1)

print("开始进行深拷贝：~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(list1)
print(list4)

print("深=====拷贝后列表id：")
print(id(list1))
print(id(list4))

print("深=====拷贝后，列表中值的变化：")
#          不可变          不可变         可变
print(id(list1[0]),id(list1[1]),id(list1[2]))
print(id(list4[0]),id(list4[1]),id(list4[2]))

list1[0]='EGON'
list1[1]='LXX'
list1[2][0]=111
list1[2][1]=222

print("修改值后，列表信息展示：")
print(list1)
print(list4)

print("修改值后深拷贝后列表id：")
print(id(list1))
print(id(list4))

print("修改值后，列表中值的id变化：")
print(id(list1[0]),id(list1[1]),id(list1[2]))
print(id(list4[0]),id(list4[1]),id(list4[2]))

'''
总结：如果拷贝一个列表，并且改操作完全独立开，就需要使用深拷贝！
'''