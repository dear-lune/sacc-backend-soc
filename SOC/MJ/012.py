def process_account(account_name,account_password,nickname):
    account_name = account_name.strip()
    if not account_name or account_name.strip() == "":
        return "账号名不能为空"
    if account_name in account_password:
        return "风险高危"
    if "退款"in nickname:
        nickname = nickname.replace("退款","***")
        return "昵称有敏感词，已替换为：{}".format(nickname)
    user_name=nickname if nickname else account_name
    welcome_message=f"Hello World! 欢迎{user_name}"
    return welcome_message

if __name__ == "__main__":
    print(process_account("      GGB ","123456GGB","退款123"))
    print(process_account("      GGB ","123456","GGB"))