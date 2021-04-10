
# 1. 基本使用

# not：就是把紧跟其后的那个条件结果取反
# ps:not与紧跟其后的那个条件是一个不可分割的整体

print(not 15>10)
print(not True)
print(not False)
print(not 10)


# and：逻辑与，and用来链接左右两个条件，必须两个条件同时为True，最终结果才为真。

print("="*20)
print(True and 10 >3)  # 条件全为真，最终结果才为True
print(10>3 and 10 and 0 and 1>3 and 3!=3)  # 偷懒原则（短路运算）


# or：逻辑或，or用来链接左右两个条件，两个条件但凡有一个为True，最终结果就是True
#           两个条件都是False的情况下，最终结果才是False

print("="*20)
print(10 or 3!=2 or 3>2 or True)  # 偷懒原则（短路运算）


# 2. 优先级  not>and>or
# ps：如果单独就只是一串and链接，或者说单独就只是一串or链接，按照从左到右的顺序依次运算即可（偷懒原则）
# 如果混用，就需要考虑优先级

# 3>4 and not 4>3 or 1==3 and 'x' =='x' or 3>3

# 尽量用括号进行标识优先级
res = (3>4 and (not 4>3)) or (1==3 and 'x' =='x') or 3>3
print(res)
res1 = 3>4 and (not 4>3 or 1==3) and ('x' =='x' or 3>3)
print(res1)

# 3. 成员运算符
print("egon" in "hello egon")  # 判断一个字符串是否存在于一个大字符串中

print(111 in [111,222,333])  # 判断元素是否存在于列表

print('k1' in {'k1':111,'k2':222})  # 判断元素是否存在于列表

# not in
print('egon' not in 'hello egon')  # 推荐使用
print(not'egon'  in 'hello egon')  # 逻辑同上，但语义不明确，不推荐，不顺畅


# 4. 身份运算符
# is # 判断的是id是否相等，内存地址是不是一样

