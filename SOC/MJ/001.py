"""
小目标1:
语言版本:Python 3.14.4
运行命令:python3 MJ/001.py
文件名:001.py


小目标2:
我想完成： 写一个 Python 脚本，让用户输入两个数字并打印它们的和。
我现在怎么写：
python
num1 = input("请输入第一个数字: ")
num2 = input("请输入第二个数字: ")
print(num1 + num2)
运行命令： python add.py
报错或输出： 输入 1 和 2 后，程序打印出了 12,而不是 3。
我尝试过： 我以为是 print 的问题，换成了 print(int(num1) + int(num2))，结果就正确了，但不知道为什么之前的会拼接在一起。
我怀疑： input() 接收到的数据类型默认是字符串，所以加号变成了拼接


小目标3:
报错名称： NameError: name 'python' is not defined
大概在骂： “名字叫 'python' 的东西没定义”。
哪里不对、怎么定位：
NameError指向的代码：python --version。
原因： 把 Python 代码环境（>>>)和系统终端环境搞混了。python --version 是给系统终端用的命令。
在 >>> 里,python 和 version 被当成变量名了，因为没有定义过这两个变量，所以报错。


小目标4：
方法名：str.strip()
作用：去除原字符串开头和结尾的空白字符（包括空格、制表符、换行符等）。如果指定了参数，则移除参数中包含的字符。
参数：可选参数 chars,表示要移除的字符集合。如果不指定,则默认移除空白字符。
返回值：返回一个新的字符串，原字符串不变。
"""
print(str.strip("  hello world  ")) 
print("  hello world  ".strip()) 
# print(str.strip("  hello world  ", chars="d"))  不能用chars="d"传参
print("  hello world ".strip(" d"))
