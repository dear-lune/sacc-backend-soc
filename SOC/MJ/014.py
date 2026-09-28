from concurrent.futures import ThreadPoolExecutor
import threading
import time
import random
success_count = 0
lock = threading.Lock()

def create_account(account_name):
    global success_count
    time.sleep(random.randint(1, 5))
    if random.randint(1, 10) > 5:
        with lock:
            success_count += 1
        print(f"账号{account_name}创建成功")
    else:
        print(f"账号{account_name}创建失败")

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=10) as executor:
        for i in range(10):
            executor.submit(create_account, i)
    print(f"成功创建{success_count}个账号")

