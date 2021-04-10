

l = [111,222,333]
l2 = l  # 把l的内存地址给l2


l[0] = 'balabala'

print(l)

print(l2)

l2[1] = 444444444

print(l2)

print(l)



del l2


# 格式化输出%
print('成功的概率 %s%%' %(97))  # 百分号在字符串中是有特殊意义的。需要两个%


# str.format()的用法
# 新用法（了解）
print('{x}======='.format(x='开始执行'))  # 开始执行=====

print('{x:=<10}'.format(x='开始执行'))  # 开始执行 左对齐
print('{x:=>10}'.format(x='开始执行'))  # 开始执行 右对齐
print('{x:=^10}'.format(x='开始执行'))  # 开始执行 中间对齐


# 四舍五入
print('{salary:.3f}'.format(salary=123456.123568))  # 精确到小数三位



# f的使用

x='egon'
y=18
res = f'name:{{{x}}},age:{y}'  # 花括号输出怎么做？写两个{}
print(res)

# 需求，人家给了字符串的10+3，但是需要计算总和。
# f 的新用法：{}内的字符串可以被当做表达式运行
res1=f'10+3'
print(res1)

res2=f'{10+3}'
print(res2)

f'{print("aaaa")}'  # 可直接被执行