import hashlib
class account:
    def __init__(self,username,nickname,password,status="active"):
        self.username=username
        self.nickname=nickname
        self.__password_hash=self.generate_hash_password(password)
        self.status=status
    def generate_hash_password(self,password):
        return hashlib.sha256(password.encode("utf-8")).hexdigest()
    def update_password(self,old_password,new_password):
        if self.__password_hash != self.generate_hash_password(old_password):
            return False,"密码错误"
        self.__password_hash=self.generate_hash_password(new_password)
        return True,"密码修改成功"
    def login(self):
        return self.status == "active"

if __name__ == "__main__":
    account1=account("admin","管理员","123456")
    print(account1.login())
    print(account1.update_password("123456","1234567"))
   
        