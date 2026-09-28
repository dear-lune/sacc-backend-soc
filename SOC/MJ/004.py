def verify_account(account_name, password, status, login_days):
    if not account_name or account_name.strip() == "":
        return "账号名不能为空"

    if len(password) < 6:
        return "密码长度不足"

    if status == "blocked":
        return "账号风险拦截"

    try:
        int(login_days)
    except:
        return "登录天数格式错误"

    return "账号校验通过"


if __name__ == "__main__":
    print(verify_account("", "123456", "active", "10"))
    print(verify_account("user1", "123", "active", "10"))
    print(verify_account("user1", "123456", "blocked", "10"))
    print(verify_account("user1", "123456", "active", "abc"))
    print(verify_account("user1", "123456", "active", "10"))
