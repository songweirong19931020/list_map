"""
@File : mysum.py
@copyright : Administrator
@Coder: Leslie_s
@Date: 2020/3/4 15:07
@Idea: PyCharm 
"""
from functools import reduce
# come on baby,简洁的完成 所有列表和相加或者相乘
myreduce = reduce((lambda x,y : x+y),[1,2,3,4,5])

#filter函数，往往和map搭配使用，主要为过滤
result =  list(filter((lambda x:x>0),range(-5,5)))

##当for循环遇上lambda

list_lm = [x+y for x in range(0,6) for y in range(0,6)]

#baby让我们在上面例子里加入if进行娱乐ok?,map的调用比for快两倍以上

list_if = [x + y for x in range(0,10) if x % 2 == 0 for y in range(0,10) if y % 2 == 1 ]
