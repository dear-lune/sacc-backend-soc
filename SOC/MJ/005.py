account_list=["","XYY001","GGB001","risk_user","GGB002","GGB003"]
success_count=0
for account in account_list:
    if not account or account.strip()=="":
        print("跳过，不计入成功处理数量")
        continue

    if account =="risk_user":
        print("风险账号，停止处理")
        break

    print(f"正在创建账号：{account}")
    success_count += 1
print(f"成功处理了{success_count}个账号")


