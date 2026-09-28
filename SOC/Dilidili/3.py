class User:
    def watch(self):
        print("观看普通视频")

class VipUser(User):
    def watch(self):
        print("观看VIP视频")

if __name__ == '__main__':
    normal_user = User()
    vip_user = VipUser()
    users = [normal_user, vip_user]

    for user in users:
        user.watch()