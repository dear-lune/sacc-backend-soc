class Video:
    def __init__(self,title,author,views,likes):
        self.title = title      
        self.author = author    
        self.views = views     
        self.likes = likes 

    def video_info(self):
        print(f"视频标题: {self.title}")
        print(f"up主: {self.author}")
        print(f"播放量: {self.views}")
        print(f"点赞数: {self.likes}")

    def get_likes(self):
        return self.likes
    def set_likes(self, new_likes):
        if new_likes < 0:
            print(f"[ERROR] 点赞数 '{new_likes}' 不能为负数。")
        else:
            self.likes = new_likes

    def add_likes(self):
        self.likes += 1
        print(f"点赞成功!当前点赞数: {self.likes}")

if __name__ == "__main__":
    video1 = Video("Python教程", "小明", 1000, 50)
    video1.video_info()
    video1.add_likes()
    video1.set_likes(60)
    print(f"更新后的点赞数: {video1.get_likes()}")