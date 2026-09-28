import os
text_name="slowfoot_accounts.txt"
def write_file(account_name,nickname,password,result):
    try:
        with open(text_name, "w") as file:
            record=account_name+" "+nickname+" "+password+" "+result
            file.write(record)
            print("写入成功")
    except Exception as e:
        print("写入失败")

def read_file():
    if os.path.exists(text_name)==False:
        print("文件不存在")
        return
    try:
        with open(text_name, "r") as file:
            for line in file:
                print(line.strip())

    except Exception as e:
        print(f"读取失败:{e}")

if __name__ == "__main__":
    while True:
        print("1.写入文件")
        print("2.读取文件")
        print("3.退出")
        choice=input("请选择：")
        if choice=="1":
            account_name=input("请输入账号：")
            nickname=input("请输入昵称：")
            password=input("请输入密码：")
            result=input("请输入结果：")
            write_file(account_name,nickname,password,result)
        elif choice=="2":
            read_file()
        elif choice=="3":
            break
        else:
            print("无效的选择")