def validateAccount(account_name,password):
    if not account_name or account_name.strip()=="":
        print("账号名不合法")
        return False
    if len(password) <6:
        print("密码不合理，太短了")
        return False
    return True

def encryptPassword(password):
    reverse_password =password[::-1]
    replace_password=reverse_password.replace("1","b")
    new_password="SOC"+replace_password
    return new_password

def buildWelcomeMessage(account_name):
    return f"Hello World!账号{account_name}诞生了"

if __name__ =="__main__":
    account_name="XYY"
    password="123456"
    judge_info=validateAccount(account_name,password)
    if judge_info:
        encrypt_password=encryptPassword(password)
        welcome_message=buildWelcomeMessage(account_name)
        print(f"{welcome_message}")
    else:
        print("处理异常，程序终止")
  