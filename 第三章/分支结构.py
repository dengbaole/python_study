# 分支结构  
money = 1000  
s = int(input("请输入取款余额："))  
if money >= s:  
    money = money - s  
    print("取款成功，余额为：", money)  
	
# 双分支结构  
num = int(input("请输入一个整数"))  
if num % 2 == 0:  
    print(num, "是偶数")  
else:  
    print(num, "是奇数")  
	
# 多分支结构  
score = int(input("请输入你的成绩"))  
if 90 <= score <= 100:  
    print("A级")  
elif score >= 80 and score <= 89:  
    print("B级")  
else:  
    print("C级")
	
# 分支结构的嵌套  
answer = input("你是会员吗? y/n")  
if answer == 'y':  
    print("会员")  
    if money >= 200:  
        print("打八折，付款金额为：", money * 0.8)  
    elif money >= 100:  
        print("打九折，付款金额为：", money * 0.9)  
    else:  
        print("不打折，付款金额为：", money)  
else:  
    print("不是会员,付款金额为：", money)	



#条件表达式
num_a = int(input("请输入第一个整数"))  
num_b = int(input("请输入第二个整数"))  
  
print("使用条件表达式比较")  
print(str(num_a)+"大于等于"+str(num_b) if num_a >= num_b else str(num_a)+"小于"+str(num_b))   # 当条件满足执行前面的语句否则后面