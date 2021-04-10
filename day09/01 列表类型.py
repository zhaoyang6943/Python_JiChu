# 1. 作用
#     按位置存放多个值，索引对应值，索引反应是位置和顺序
#     多个人的姓名，多个人的信息
# 2. 定义
#     中括号内放多个任意类型的值
#     l=[1,1.1,'a']
# 3. 类型转换
#     但凡能够被for循环遍历的类型都可以当做参数传给list()转成列表
# res=list('hello')
# print(res)
# 等于下面5行的代码，上面两行代码搞定！
# a='hello'
# l=[]
# for i in a:
#     l.append(i)
# print(l)


# 字典类型转换(有序字典。。)
# res = list({"k1":"aaa","k2":"bbb","k3":"ccc"})
# print(res)

# 4. 内置方法

# ===========优先掌握==========的操作：

# 4.1 按索引存取值（正向取值+反向取值）：既可以取（不是增加）也可以改
# l=[111,'egon','hello']
# 正向取
# print(l[1])
# 反向取
# print(l[-1])

# 可以取也可以改：索引存在则修改对应的值
# l[0]=222
# print(l)

# 无论是取值操作还是赋值操作：索引不存在则报错(越界！！！！)
# l[3]=333


# 4.2 切片（顾头不顾尾）；切片是一种拷贝行为，并不改变原来的值；相当于浅拷贝！！！
# l=[111,'egon','hello','a','b','c','d',[1,2,3]]

# print(l[1:5])  # 第二到第五个值取出来，取出的格式还是列表
# print(l[1:5:2])  # 第二到第五值，每隔两个取出一个值

# 通过切片方式复制这个列表
# print(l[0:len(l)])
# print(l[:])  # 默认开始和结束是最开始和结束

# 浅拷贝验证
# new_l = l
# l[-1][0]="1111111"
# print(l)
# print(new_l)

# 把列表整个倒过来，和字符串一样
# print(l[::-1])


# 4.3 长度
# l=[111,'egon','hello','a','b','c','d',[1,2,3]]
# print(len(l))


# 4.4 成员运算 in 和 not in
# print('aaa' in ['aaa',2])

# 4.5 追加  # 永远是在最后面添加值，如果想要在中间插入值，用insert
# l=[111,'egon','hello']
# l.append('444')
# print(l)


# 4.6 插入值
# l=[111,'egon','hello']
# l.insert(1,'444')  # 前面是索引，后面是插入的值；在一号索引插入‘444’
# print(l)


# 4.7 需求：新的列表[1,2,3],把123列表放在l后面；
# new_l=[1,2,3]
# l=[111,'egon','hello']
# l.append(new_l)  # 但是注意了，这样增加的是在列表中添加列表[111, 'egon', 'hello', [1, 2, 3]]；没有达到我想要的目的
# print(l)

# 代码实现需求：(可以实现，但是python有内置方法，不用我们重复造轮子)
# for item in new_l:
#     l.append(item)
# print(l)

# extend实现了上述代码；
# l.extend(new_l)  # 这个方法就是做了循环在new_l中遍历取值，一一添加到l列表中
# print(l)
#
# l.extend("abc")  # 字符串也可以

# 亚伦亚瑟36题：迅速增加两个人关系。。。。。。。。。。。。。。。。。。。。。。



# 4.8 删除
# 方式一：通用的删除方法，只是单纯的删除、没有返回值
# l=[111,'egon','hello']
# del l[0]
# # x=del l[1]  # 抛出异常，不支持赋值语法
# print(l)

# 方式二：l.pop 根据索引删除，默认删除最后一个
# l=[111,'egon','hello']
# l.pop()  # 默认删除最后一个
# l.pop()
# print(l)
#
# 删除后，会有返回值
# a=l.pop(0)
# print(a,type(a))


# 方式三：l.remove()根据元素删除，返回None，和del类似
# l=[111,'egon','hello',[1,2,3]]
# l.remove(111)
# print(l)
# l.remove([1,2,3])
# print(l)
#
# res = l.remove('egon')  # 拿到删除的值，但是这个返回None
# print(res)


# 4.9 循环
# for x in [1,'aaa','bbb']:
#     print(x)



# ===========需要掌握==========的操作：（ps：列表基本都是需要掌握的操作，没有了解的！）
# 注意：代码中的忌讳
# l=[1,'aaa','bbb']
# for x in l:
#     l.pop(1)  # 不要在循环中修改值，忌讳，在循环过程中，不能改in 后面的事情，只进行读行为
#     print(x)


l=[1,'aaa','bbb','bbb','bbb']


# 5.1 l.count()  # 统计元素在列表中出现的数量
# print(l.count('bbb'))

# 5.2 l.index()  # 返回索引
# print(l.index('bbb'))
# print(l.index('bbbbbb'))  # 找不到报错

# 5.3 l.clear()  # 清空列表
# l.clear()
# print(l.clear())
# print(l)

# 5.4 l.reverse()  # 不是排序，就是将列表倒过来
# l.reverse()
# print(l)

# 5.5 l.sort()  # 比较大小，只能针对列表内元素只能是数字，同种类型才能排序
# l = [1,2,5,3.1,999,55]
# l.sort()  # 默认正序排序，从小到大
# l.sort(reverse=True)  # reverse默认是False，修改为True后，降序排序，从大到小
# print(l)


# l = [1,'a',2]
# l.sort()  # 报错，不支持非同种类型的值进行排序，字符串和数字之间不能比较大小
# print(l)


# l=['a','e','c','是']
# l.sort()  # 列表中字符串的排序
# print(l)

# 了解
# 字符串可以比较大小，按照对应的位置的字符依次pk
# 字符串的大小是按照ASCI码表的先后顺序加以区别，表中排在后面的字符大于前面的
# print('a'>'b')  # 后面字符大于前面
# print('abz'>'abcdzdsf')  # 后面字符大于前面，多字符串就按照对应的位置依次pk

# 列表也能比较大小，原理同字符串一样，但是对应位置的元素必须是同种类型
# l1 = ['a','e','f',123,'aav']
# l2 = ['a','e','e',456,'qwe']
# print(l1>l2)



# 补充：队列；  堆栈   都是两种数据结构；吃了拉，吃了吐。。。
'''
队列：FIFO，先进先出
'''
l=[]
# 入队操作
l.append('first')
l.append('first2')
l.append('first3')

print(l)

# 出队操作
print(l.pop(0))
print(l.pop(0))
print(l.pop(0))


'''
堆栈：LIFO，后进先出
'''

l=[]
# 入队操作
l.append('first')
l.append('first2')
l.append('first3')

print(l)

# 出队操作
print(l.pop(-1))
print(l.pop(-1))
print(l.pop(-1))