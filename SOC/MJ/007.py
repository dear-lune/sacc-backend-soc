def validateAccount(account_name, password):
    if not account_name or account_name.strip() == "":
        return False, "账号名不能为空"
    if len(password) < 6:
        return False, "密码长度不足"
    return True, "校验通过" 

def encryptPassword(password):
    reverse_password = password[::-1]
    replace_password = reverse_password.replace("1", "b")
    return "SOC" + replace_password

def saveAccountInfo(account_name, encrypted_pwd):
    print(f"正在将账号 [{account_name}] 和密文 [{encrypted_pwd}] 写入数据库")
    return True, "保存成功"

def buildWelcomeMessage(account_name):
    return f"Hello World! 账号 {account_name} 诞生了"

def main():
    account_name = "slow_account"  
    password = "123456"
    is_valid_msg = validateAccount(account_name, password)
    if not is_valid_msg:
        print(f"流程终止：{is_valid_msg}")
        return 
    print("账号校验通过")

    encrypted_pwd = encryptPassword(password)
    print(f"密码加密完成，密文为: {encrypted_pwd}")

    save_success, save_msg = saveAccountInfo(account_name, encrypted_pwd)
    if not save_success:
        print(f"流程终止：{save_msg}")
        return
    print("账号信息保存成功")

    welcome_msg = buildWelcomeMessage(account_name)
    print(f"最终结果: {welcome_msg}")

if __name__=="__main__":
    main()