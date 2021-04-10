# 1. 垃圾回收机制详解（了解）

# 1.1 引用计数（核心）
x= 10  # 直接引用
print(id(x))

l=['a',x]  # 间接引用
print(id(l[1]))

# 管理内存，释放内存空间1. 麻烦，涉及到释放内存的操作；2. 容易导致错误，万一没有考虑周全，删除错误，会导致bug

# 问题？ 以下操作，x的值，在l中有没有发生变化！
x =10
l = ['a','n',x]     # l=['a'的内存地址,'b'的内存地址,'c'的内存地址]
x=123

print(l[2])
# del x      解除绑定

# 1.2 标记清除
# 堆区取不到的值，全部标记死亡！进行清除。效率太低

# 循环引用，
l1 = [111]
l2 = [222]

l1.append(l2)  # l1=[值111的内存地址，l2列表的内存地址]
l2.append(l1)  # l2=[值222的内存地址，l1列表的内存地址# ]

print(l1)
print(id(l1),id(l2))
print(id(l1[1]))

# 导致致命的事情,把直接引用都删除，但是间接引用都有，就形成了永远清理不了的垃圾，（引用不到）
# del l1
# del l2

# 1.3 分代回收
# 检查权重标记！
# 新生代
# 青春代
# 老生代