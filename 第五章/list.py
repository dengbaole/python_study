#
a = 10
lit = ['hello','world',10]
print(id(a))
print(id(lit))
print(lit)
print(lit[0])
print(id(lit[2]))

#列表创建的两种方式
lit = ['hello','world',10]
lit2 = list(['hello','world',10])
print(id(lit))   #两个地址相同
print(id(lit2))


#查找列表中元素的索引
print(lit.index('hello'))   #只返回第一个位置
print(lit.index('hello',0,3))  #在0到3中查找

#列表切片
#  列表名[start:stop:step]
lit =[10,20,30,40,60,80]
#步长为负数时后面遍历
print(lit[0:4:1]) 


#判断列表中是否存在元素
print(10 in lit)
print(90 in lit)
print(10 not in lit)

#列表的遍历
for item in lit:
    print(item)

#列表的增加
lit = [1,2]
#在末尾增加数字
lit.append(100)
print(lit)
#向末尾添加多个元素
lit.extend(lit)
print(lit)
#在任意位置上添加元素
lit.insert(1,10)
print(lit)


#列表中添加元素
lst=[10,20,30,40,50]
    #删除列表中的20
lst.remove(20)
print(lst) 

    #移除列表中1位置的元素
lst.pop(1)
print(lst)
    #切片操作——产生一个新的列表
new_list=lit[1:3]
print('原列表',lst)
print('切片后列表',new_list)

    #切片删除列表
lst[1:3]=[]
print(lst)
    #清空列表
lst.clear()
print(lst)

    #删除列表
del lst


    #列表的修改
lst = [10,20,30]
lst[1]=40
print(lst)

   #列表的排序
lst  = [40,10,30,1,3,5]
        #正序排序
lst.sort()
print(lst)
        #逆序排序
lst.sort(reverse=True)
print(lst)

    #列表排序并产生新列表
lst2=sorted(lst)
print(lst2)

   #列表生成式    
lst = [i*i for i in range(1,10)]
print(lst)  #每个元素为i*i,i的取值为1-9
lst = [2*i for i in range(1,10)]
print(lst)
 