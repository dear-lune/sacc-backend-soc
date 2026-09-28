num=input("请输入一个整数：")
new_num=num[::-1]
if new_num==num:
    print(True)
else:
    print(False)


# [::-1] 是字符串专用的切片语法
#因此用num=int(input("请输入一个整数："))会报错