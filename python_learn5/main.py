#集合的基本形式,集合不能使用下标索引,集合中的元素不可以重合，也不能使用下标索引,数据无序排列
# set_1 = {1,2,3,4,5,6}
# print(set_1)
#集合末尾添加一个元素
# set_1 = {1,2,3,4,5,6}
# set_1.add(7)
# print(set_1)
#移除集合中的指定元素
# set_1 = {1,2,3,4,5,6}
# set_1.remove(5)
# print(set_1)
#从集合中随机取出一个元素
# set_1 = {1,2,3,4,5,6}
# num = set_1.pop()
# print(set_1)
# print(num)
#清空集合
# set_1 = {1,2,3,4,5,6}
# set_1.clear()
# print(set_1)
#集合变换一，得到一个新集合，新集合中包含除集合一与集合二公共部分的集合一中的元素
# set_1 = {1,2,3,4,5,6}
# set_2 = {1,2,3,7,8,9}
# set_3 = set_1.difference(set_2)
# print(set_1)
# print(set_2)
# print(set_3)
#集合变换2，删除集合二在集合一中存在的元素，集合一被修改，集合二不变
# set_1 = {1,2,3,4,5,6}
# set_2 = {1,2,3,7,8,9}
# set_1.difference_update(set_2)
# print(set_1)
# print(set_2)
#得到一个新集合，内含一二两个集合全部的元素，原集合不变
# set_1 = {1,2,3,4,5,6}
# set_2 = {1,2,3,7,8,9}
# set_3 = set_1.union(set_2)
# print(set_1)
# print(set_2)
# print(set_3)
#得到一个代表集合数量的整数
# set_1 = {1,2,3,4,5,6}
# number = len(set_1)
# print(number)
#字典的定义,字典不能重复，数据无序排列
# dict_1 = {1:78,3:98,2:100,4:45}
# dict_2 = {}
# print(dict_1)
# print(dict_2)
# print(dict_1[3])
#字典的常用操作1，更新或添加键值对,添加只能添加在末尾
# dict_1 = {1:78,3:98,2:100,4:45}
# dict_1[3] = 96
# dict_1[5] = 97
# print(dict_1)
# print(dict_1[3])
#字典的常用操作2，去除key对应的Value,并删除此键值对
# dict_1 = {1:78,3:98,2:100,4:45}
# number = dict_1.pop(4)
# print(dict_1)
# print(number)
#清空字典
# dict_1 = {1:78,3:98,2:100,4:45}
# dict_1.clear()
# print(dict_1)
#获取字典的全部key，可用for循环遍历字典
# dict_1 = {1:78,3:98,2:100,4:45}
# for i in dict_1.keys():
#     print(dict_1[i])
#计算字典的元素数量
# dict_1 = {1:78,3:98,2:100,4:45}
# number = len(dict_1)
# print(dict_1)
# print(number)
#练习1
# dict_1 = {"王力宏":{"部门":"科技部","工资":3000,"级别":1},"周杰伦":{"部门":"市场部","工资":5000,"级别":2},
#           "林俊杰":{"部门":"市场部","工资":6000,"级别":3},"张学友":{"部门":"科技部","工资":4000,"级别":1},
#           "刘德华":{"部门":"市场部","工资":6000,"级别":2}}
# print(dict_1)
# dict_1["王力宏"]["工资"] = 4000
# dict_1["王力宏"]["级别"] = 2
# dict_1["张学友"]["工资"] = 5000
# dict_1["张学友"]["级别"] = 2
# print(dict_1)
#容器的通用功能
#通用for循环遍历
#max()
#min()
#len()
#list()
#touple()
#str()
#set()
#sorted(序列，[reverse=Ture])    得到一个排好序的序列，Ture表示降序
