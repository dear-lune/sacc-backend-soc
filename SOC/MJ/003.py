account_name = input("请输入账号：")
name=input("请输入昵称：")
password=input("请输入密码：")
login_days=int(input("请输入连续登录天数："))
user_input = input("是否为新用户（是/不是）：")
if user_input != "是" and user_input != "不是":
    print("输入错误！只能输入'是'或'不是'。")
else:
    is_new_user=(user_input == "是")

login_counts = [3, 5, 2, 8, 4, 6, 7] 

# 第 1 天的登录次数
print(f"第 1 天登录次数: {login_counts[0]}")

# 获取第 7 天的登录次数
print(f"第 7 天登录次数: {login_counts[6]}")

# 一共记录了多少天=
print(f"一共记录了多少天: {len(login_counts)} 天")

#修改第三天结果
login_counts[2]=32
print(f"第三天的登录次数更新为：{login_counts[2]}")


#输出资料卡
print(f"账号名：{account_name}")
print(f"昵称：{name}")
print(f"登录天数：{login_days}")
print(f"新用户：{is_new_user}")
