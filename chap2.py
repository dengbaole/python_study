#变量
massage = "hello python!"
print(massage)



#用方法输出字符串格式（方法的使用 变量名.方法）
name = "dengbaole"
#输出标题
print(name.title())
#输出大写
print(name.upper())
#输出小写
print(name.lower())


#合并字符串
first_name = "ada" 
last_name = "lovelace" 
full_name = first_name + " " + last_name # => "ada"+" " +"lovelace"

print(full_name)



#制表符和换行符
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")


#删除空格
favorite_language = ' python ' 
#删除右边空格
print(favorite_language.rstrip()) 
#删除左边空格
print(favorite_language.lstrip() )
#删除所有空格
print(favorite_language.strip())


#整数运算
print(2**3)  #2三次方
print(2*3)

#生成
fp=open('D:/test.txt','a+')
print('helloworld',file=fp)
fp.close()