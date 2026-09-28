import hashlib
class Account:
    def __init__(self, name, password_hash, status="active"): 
        self.name = name
        self.__password_hash = password_hash  
        self.status = status
    def get_password_hash(self):
        return self.__password_hash
 

class PasswordHasher:
    @staticmethod
    def generate_hash(password):
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

class account_manager:
    def __init__(self):
        self._accounts = [] 

    def save(self, account):
        self._accounts.append(account)
        print(f"账号 {account.name} 已保存。")

    def get_all(self):
        return self._accounts

class Notifier:
    @staticmethod
    def send_notification():
        print("Hello World!") 

def main():
    password_hash = PasswordHasher.generate_hash("password")
    account = Account("admin", password_hash)
    manager = account_manager() 
    manager.save(account)
    
    accounts = manager.get_all()
    
    for account in accounts:
        print(f"{account.name} 的密码哈希值为 {account.get_password_hash()}")
    Notifier.send_notification()
if __name__ == "__main__":
    main()
