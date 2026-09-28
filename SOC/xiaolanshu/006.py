class Note:
    def __init__(self, tittle,likes):
        self.tittle = tittle
        self.likes = likes
    def addLike(self):
        self.likes += 1
    def getInfo(self):
        return f"{self.tittle} : {self.likes}"

tittle = input("笔记标题：")
likes = int(input("点赞数："))
try:
    n=int(input())
    if n<1 :                      #在这里写type(n) != int)没有用，因为上一行强制了int
        print("笔记数量不合法,重新输入")
    else:
        note = Note(tittle,likes)
        for _ in range(n):
            note.addLike()
        print(note.getInfo())
except ValueError:
    print("输入无效，请输入一个整数。")