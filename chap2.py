#����
massage = "hello python!"
print(massage)



#�÷�������ַ�����ʽ��������ʹ�� ������.������
name = "dengbaole"
#�������
print(name.title())
#�����д
print(name.upper())
#���Сд
print(name.lower())


#�ϲ��ַ���
first_name = "ada" 
last_name = "lovelace" 
full_name = first_name + " " + last_name # => "ada"+" " +"lovelace"

print(full_name)



#�Ʊ���ͻ��з�
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")


#ɾ���ո�
favorite_language = ' python ' 
#ɾ���ұ߿ո�
print(favorite_language.rstrip()) 
#ɾ����߿ո�
print(favorite_language.lstrip() )
#ɾ�����пո�
print(favorite_language.strip())


#��������
print(2**3)  #2���η�
print(2*3)

#����
fp=open('D:/test.txt','a+')
print('helloworld',file=fp)
fp.close()