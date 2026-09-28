import hashlib
from datetime import datetime
from dataclasses import dataclass
@dataclass
class AccountTemplate:
    username: str
    nickname: str
    password_hash: str
    status: str
    create_time: str
    def show_info(self):
        print(f"用户名：{self.username}")
        print(f"昵称：{self.nickname}")
        print(f"密码：{self.password_hash[:6]}...")
        print(f"状态：{self.status}")
        print(f"创建时间：{self.create_time}")

my_acount=AccountTemplate("XYY001","小蓝","123as45ds6w","正常","2026-09-28 15:30:00")
my_acount.show_info()