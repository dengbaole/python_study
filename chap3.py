
#变量的定义
name  ='玛利亚'   #变量保存的是地址？地址中有数据类型等相关信息
print(name)
print('标识',id(name))   #地址
print('类型',type(name))
print('值',name)


#数据类型
    ## 整数类型
        #可以标识正数，负数，0
n1 = 30
n2 = -32
n3 = 0
print(n1)
print(n2)
print(n3)

print('十进制',118)
print('二进制',0b1010111)
print('八进制',0o1660)
print('十六进制',0xff)

        ##浮点数
n1 = 0.1
n2=0.2
print(n1+n2)  #不精确（需要导入模块计算精确值）

        ##布尔类型
f1=True
f2=False
print(f1,type(f1))
print(f2,type(f2))

        ##字符串类型
string1 = '''hello
hellloooooooooooooooo'''   #三引号可以多行显示
print(string1)


##数据类型转换
a=10
b=198.8
c=False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c))     #转换成字符类型


#输入函数
