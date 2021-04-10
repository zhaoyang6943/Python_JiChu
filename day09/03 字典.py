# 1. 作用
#     key对应值

# 2. 定义：{}内用逗号分割开多个key：value，其中value可以是任意类型，
#       但是key必须是不可变类型,且不可重复

# 2.1
# d = {'k1':111,'k2':'222','k3':0.1,(1,):None}  # d=dict(...)
# print(d['k1'])
# print(d[(1,)])
# print(type(d))

# 2.2
# d={}  # 默认定义出来的是空字典，集合需要另外注意
# print(d,type(d))

# 2.3
# d=dict(x=1,y=2,z=3, 搜索=5,)
# print(d,type(d))

# 3. 数据类型转换
# 需求，列表中存的人的信息，把列表中元素取出来，key对应value的方式
info = [
    ['name','yang'],
    ('age',18),
    ['gender','male']
]
# 方法一：
# d={}
# for item in info:
#     # print(item)
#     d[item[0]]=item[1]
# print(d)

# 方法二：
# d={}
# for k,v in info:
#     d[k]=v
# print(d)

# 方法三：  # dict 直接将这样的列表转为了字典，推荐使用
# for循环这样的列表，这个列表必须有两个值，才能数据类型转换
# res = dict(info)
# print(res)

# 需求：造字典的方式，快速初始化一个字典
# key值是列表的值，value是默认的None值
keys=['name','age','gender']
# 方法一：
# d={}
# for i in keys:
#     d[i]=None
# print(d)


# 方法二：就相当于for循环循环列表中的值，
# d={}.fromkeys(keys,None)
# print(d)

# 4. 内置方法

# 优先掌握的操作：====================================

# 4.1 按key存取值：可存可取。
d={'k1':111}
# 针对赋值操作：key 存在，则修改
# d['k1'] = 222
# print(d)
# 针对赋值操作：key 不 存 在，则 创建新值
# d['k2'] = 5555
# print(d)


# 4.2 长度len
# d= {'k1':111,'k2':'222','k3':0.1,(1,):None,'k1':'123'}
# print(d)
# print(len(d))  # 当字典中有重复key值时，只取一个，所以字典中key值不要重复！！！


# 4.3 成员运算 in 和 not in ，根据key
# d={'k1':111,'k2':'222','k3':0.1}
# print('k1' in d)


# 4.4 删除
d={'k1':111,'k2':'222','k3':0.1}
# 方法一：
# del d['k1']
# print(d)

# 方法二：pop删除，根据key删除元素，返回删除的key对应的value值
# res = d.pop('k2')
# print(d)
# print(res)

# 方法三：popitem删除：随机删除，返回元组（删除的key，删除的value）
# res = d.popitem()
# print(d)
# print(res)


# 4.5 键 keys()， 值 values()，键值对 item()  ==>> 在python3中得到老母鸡
# 这是python2下执行的，但是有一个不好之处，如果字典有一万个，就很消耗内存了
'''
>>> d={'k1':111,'k2':222}
>>> d.keys()
['k2', 'k1']
>>> d.values()
[222, 111]
>>> d.items()
[('k2', 222), ('k1', 111)]
>>> dict(d.items())
{'k2': 222, 'k1': 111}

'''

# for循环，python3中老母鸡，每次只取一个！！
# d={'k1':111,'k2':'222','k3':0.1}
# for k in d.keys():
#     print(k)
#
# for v in d.values():
#     print(v)
#
# for k,v in d.items():
#     print(k,v)

# 思考？想key转为Python2那样，怎么做？  直接列表转换就行了
# print(list(d.keys()))
# print(list(d.values()))
# print(list(d.items()))


# 需要掌握的内置方法：====================================
d={'k1':111,'k2':'222','k3':0.1}

# 4.6 d.clear() 清空字典
# print(d.clear())

# 4.7 d.update()
# d.update({'k1':'aaa','k2':'bbb','k3':'ccc','k4':'ddd'})
# print(d)

# 4.8 d.get() :根据key取值，容错性好
# print(d['k6'])  # 不存在则报错

# print(d.get('k1'))
# print(d.get('k6'))  # key值不存在不报错，返回None


# 4.9 d.setdefault()  如果字典中有这个key值，则不添加；返回字典中key对应的值
d={'k1':111,'k2':'222','k3':0.1}
res = d.setdefault('k1',222)
print(res)

# 如果key没有则添加，返回字典中key对应的值
d={'k1':111,'k2':'222','k3':0.1}
res = d.setdefault('k4','dddddd')
print(res)
print(d)