from dataclasses import dataclass
@dataclass
class AccountTemplate:
    username: str
    nickname: str
    password_hash: str
    status: str
    create_time: str

account1=AccountTemplate('MYY','MYY','123456','normal','2020-01-01')
account2=AccountTemplate('XYY','XYY','12344556','normal','2020-09-01')
account3=AccountTemplate('LYY','LYY','1234564456','activel','2023-01-01')
account4=AccountTemplate('BYY','BYY','123456446','normal','2025-01-01')
account5=AccountTemplate('JYY','JYY','123456456','active','2026-01-01')

account_list=[account1,account2,account3,account4,account5]

account2.status = "active"
for account in account_list:
    print(account.username,account.nickname,account.password_hash,account.status,account.create_time)