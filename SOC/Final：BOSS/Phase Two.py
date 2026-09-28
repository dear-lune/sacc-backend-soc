class content:
    def __init__(
        self, title, author, platform, views, comments, likes, shares, saves, tags
    ):
        self.__title = title
        self.__author = author
        self.__platform = platform
        self.__views = views
        self.__comments = comments
        self.__likes = likes
        self.__shares = shares
        self.__saves = saves
        self.__tags = tags

        try:
            self.__views = int(views)
        except ValueError:
            print(f"[ERROR] 播放量 '{views}' 格式错误，自动设为 0。")
            self.__views = 0

    def getTitle(self):
        return self.__title

    def setViews(self, new_views):
        if new_views < 0:
            print(f"[ERROR] 观看量 '{new_views}' 不能为负数。")
        else:
            self.__views = new_views

    def getPlatform(self):
        return self.__platform

    def getViews(self):
        return self.__views

    def getLikes(self):
        return self.__likes

    def getComments(self):
        return self.__comments

    def getShares(self):
        return self.__shares

    def getSaves(self):
        return self.__saves
    def getTags(self):
        return self.__tags

    def getInfo(self):
        print(
            "作者：",
            self.__author,
            "平台：",
            self.__platform,
            "观看量：",
            self.__views,
            "评论量：",
            self.__comments,
            "点赞量：",
            self.__likes,
            "分享量：",
            self.__shares,
            "收藏量：",
            self.__saves,
            "标签：",
            self.__tags,
        )


# 测试
# if __name__ == "__main__":
#     item=content("标题1","作者1","平台1",1000,50,200,30,10,["标签1","标签2"])
#     item.getInfo()
#     print("标题：", item.getTitle())
#     print("修改标题为：标题2")
#     item.setTitle("标题2")
#     print("标题：", item.getTitle())


class creator:
    def __init__(self, name, followerCount):
        self.__name = name
        self.__followerCount = followerCount
        self.__contentCount = 0
        self.__totalTrafficScore = 0

    def add_content(self, views):
        self.__contentCount += 1
        self.__totalTrafficScore += views

    def get_contentCount(self):
        return self.__contentCount

    def get_totalTrafficScore(self):
        return self.__totalTrafficScore

    def get_creatorLevel(self):
        score = self.__totalTrafficScore
        if score >= 1000000:
            return "平台顶流"
        elif score >= 50000:
            return "热门创作者"
        elif score >= 10000:
            return "潜力创作者"
        else:
            return "新人创作者"


class platform:
    def calculateTrafficScore(self, content):
        raise NotImplementedError("子类必须重写 calculateTrafficScore 方法！")


# 有状态（需要存数据）的类，必须写 __init__ 来初始化状态。# 纯逻辑（只负责干活）的类，可以省略 __init__，直接写方法。
# 不能用Pass,可能返回None，不报错


class DStationPlatform:
    def calculateTrafficScore(self, content):
        traffic_score = (
            content.getViews() * 0.3
            + +content.getLikes() * 2
            + content.getComments() * 4
            + content.getSaves() * 6
        )
        return traffic_score


class TiaoYinPlatform:
    def calculateTrafficScore(self, content):
        traffic_score = (
            content.getViews() * 0.4
            + content.getComments() * 2
            + content.getLikes() * 3
            + content.getShares() * 5
        )
        return traffic_score


class BlueBookPlatform:
    def calculateTrafficScore(self, content):
        traffic_score = (
            content.getViews() * 0.3
            + content.getLikes() * 2
            + content.getComments() * 3
            + content.getSaves() * 8
        )
        return traffic_score


class SlowFootPlatform:
    def calculateTrafficScore(self, content):
        traffic_score = (
            content.getViews() * 0.4
            + content.getLikes() * 2
            + content.getComments() * 5
            + content.getShares() * 3
        )
        return traffic_score


class TrafficAnalyzer:
    def __init__(self, content_list):
        self.content_list = content_list

    def platformAverages(self):
        platform_names = ["D站", "跳音", "小蓝书", "慢脚"]
        for p_name in platform_names:
            total_score = 0  
            count = 0        
            for content in self.content_list:
                if content.getPlatform() == p_name:
                
                    if p_name == "D站":
                        rule = DStationPlatform()
                    elif p_name == "跳音":
                        rule = TiaoYinPlatform()
                    elif p_name == "小蓝书":
                        rule = BlueBookPlatform()
                    elif p_name == "慢脚":
                        rule = SlowFootPlatform()
                    else:
                        rule = None
                    if rule:
                        score = rule.calculateTrafficScore(content)  # 加上 rule.
                        total_score += score
                        count += 1
            if count > 0:
                avg = total_score / count
                print(f"平台: {p_name} , 平均分: {avg:.2f}")   #{avg:.2f} 里面的 .2f 意思是保留两位小数
            else:
                print(f"平台: {p_name} , 暂无数据")


    def analyzeTraffic(self):
        max_score=-1
        ranking_list = []
        tag_count = {}
        for content in self.content_list:
            platform_name = content.getPlatform()
            if platform_name not in ["D站", "跳音", "小蓝书", "慢脚"]:
                print(f" 检测到不合法平台 '{platform_name}'，跳过。")
                continue
            if platform_name == "D站":
                platform = DStationPlatform()
            elif platform_name == "跳音":
                platform = TiaoYinPlatform()
            elif platform_name == "小蓝书":
                platform = BlueBookPlatform()
            elif platform_name == "慢脚":
                platform = SlowFootPlatform()
            else:
                print(f"[ERROR]未知平台: {platform_name}")
                continue

            traffic_score = platform.calculateTrafficScore(content)
            title=content.getTitle()
            title_includes=" (包含'后端'关键词)" if "后端" in title else ""

            print(f"标题: {title.strip()} {title_includes},流量分数: {traffic_score}")

            if traffic_score > max_score:
                max_score = traffic_score
                max_content_title = content.getTitle()    

            ranking_list.append((traffic_score, content.getTitle()))

        ranking_list.sort(key=lambda x: x[0], reverse=True)
        print("\n流量分数排名:")
        for rank, (score, title) in enumerate(ranking_list[:3], start=1):
            print(f"TOP{rank}: {title.strip()}, 分数: {score}")

        print(f"流量分数最高的内容标题: {max_content_title.strip()}, 分数: {max_score}")

    def getTagCount(self):
        tag_count = {}
        for content in self.content_list:
            for tag in content.getTags():
                if tag in tag_count:
                    tag_count[tag] += 1
                else:
                    tag_count[tag] = 1
        for tag, count in tag_count.items():
            print(f"{tag}: {count} 条")
        


if __name__ == "__main__":
    content1 = content(
        "  标题1", "作者1", "D站", 1000, 50, 200, 30, 10, ["休闲", "后端"]
    )
    print(f"[INFO] 添加内容：{content1.getTitle()}")
    content2 = content(
        "标题2  ", "作者2", "跳音", 2000, 100, 300, 50, 20, ["前端", "抽象"]
    )
    print(f"[INFO] 添加内容：{content2.getTitle()}")
    content3 = content(
        "三分钟get后端", "作者3", "小蓝书", 1500, 80, 250, 40, 15, ["后端", "学习"]
    )
    print(f"[INFO] 添加内容：{content3.getTitle()}")
    content4 = content(
        "标题4", "作者4", "慢脚", 1200, 60, 220, 35, 12, ["SOC", "学习"]
    )
    print(f"[INFO] 添加内容：{content4.getTitle()}")
    content5 = content(
        "标题5", "作者5", "慢脚", 800, 40, 180, 25, 8, ["抽象", "后端"]
    )
    print(f"[INFO] 添加内容：{content5.getTitle()}")

    content_list = [content1, content2, content3, content4, content5]
    analyzer = TrafficAnalyzer(content_list)
    analyzer.analyzeTraffic()
    content3.setViews(-999)
    analyzer.platformAverages()
    analyzer.getTagCount()


    
