'''
不可变的列表，只用来读，不用来改
'''
# 1. 作用
#     按位置/索引存放多个值，只用于读，不用于改

# 2. 定义： （）内用逗号分隔开多个任意类型的元素
# t=('a',1,(1))
# print(t,type(t))

# 单独一个括号，代表包含的意思，如果元组中只有一个值，后面一定要加逗号
# a=(10)
# print(a,type(a))  # 这个是int类型

# b=(10,)
# print(b,type(b))  # 这个是元组

# 验证元组不可改
# t=('a',1,1.2,'啊')  # t=(a->对应a的内存地址，1对应1的内存地址，1.2对应1.2的内存地址，啊对应啊的内存地址)
# # t[0] =123  # 会报错，提示元组不支持修改类型
# print(t)

# 但是如果元组中有列表，就可以修改列表中信息(类似浅拷贝的样子)
# t1=(1,['11','22'])
# print(t1[0],t1[1])
# print(id(t1[0]), id(t1[1]))
# t1[1][0] = "aaaaa"
# print(t1[0],t1[1])
# print(id(t1[0]), id(t1[1]))


# 3. 类型转换
# 但凡能够被for循环遍历的类型都可以当做参数传给list()转成元组
# res=tuple('hello')
# print(res)
# res = tuple({"k1":"aaa","k2":"bbb","k3":"ccc"})
# print(res)

# 4. 内置方法


# 4.1 按索引取值（正向取 + 反向取）：只能取
# t=('aa','bb','cc')
# print(t[0])
# print(t[1])


# 4.2 切片（顾头不顾尾，步长）
# t=('aa','bb','cc','dd','eee')
# print(t[0:1])
# print(t[::-1])


# 4.3 长度
# t=('aa','bb','cc','dd','eee')
# print(len(t))


# 4.4 成员运算 in 和 not in
# t=('aa','bb','cc','dd','eee')
# print('aa' in t)


# 4.5 循环
# t=('aa','bb','cc','dd','eee')
# for x in t:
#     print(x)


# 4.6 index 索引,根据值，返回索引
# t=('aa','bb','cc','dd','eee')
# print(t.index("aa"))


# 4.7 count 数量，计算值在元组中出现的个数
# t=('aa','bb','cc','dd','eee','aa')
# print(t.count("aa"))