#生成一个整数序列 range优点在用到的时候才会生成，不用到的话每个range在内存中占用的空间相同
r = range(10)   #从0开始步长为1，到10结束
print(r)
print(list(r))

r = range(1,10)   #从1开始步长为1，到10结束
print(r)
print(list(r))

r = range(1,10,2)   #从0开始步长为2，到10结束
print(r)
print(list(r))