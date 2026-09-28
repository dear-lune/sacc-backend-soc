#欢迎信息
print("欢迎来到跳音流量观察台")
print("当前身份：后端组 SOC 实习生")
print("负责人：yantz")


content_list = []
while True:
    print("\n请选择你要进行的操作：")
    print("1. 添加一条内容数据")
    print("2. 查看所有内容数据")
    print("3. 计算并展示流量等级")
    print("4. 搜索指定标题或作者")
    print("0. 退出系统")
    choice = int(input("请输入操作编号："))
    if choice == 0:
        print("退出系统，感谢使用！")
        break
    if choice == 1:
        title = input("请输入内容标题：")
        author = input("请输入内容作者：")
        platform = input("请输入内容平台：")
        views = int(input("请输入内容观看量："))
        comments = int(input("请输入内容评论量："))
        likes = int(input("请输入内容点赞量："))
        shares= int(input("请输入内容分享量："))
        saves=int(input("请输入收藏量："))
        tags = input("请输入内容标签（用逗号分隔）：").split(",")
        content_list.append({"title": title, "author": author, "platform": platform, "views": views, "comments": comments, "likes": likes, "shares": shares, "saves": saves, "tags": tags})
        print("内容数据已添加！")

    if choice == 2:
        if not content_list:
            print("	没数据，自己加！")
        else:
            print("所有内容数据如下：")
            for content in content_list:
                print(content)

    if choice == 3:
        if not content_list:
            print("	没数据，自己加！")
        else:
            print("流量等级计算结果如下：")
            for content in content_list:
                traffic_score = content["views"] * 0.4+ content["comments"] *3+ content["likes"] * 2+ content["share"] * 4 + content["saves"] * 5
                if traffic_score >= 200000:
                    traffic_level = "爆款候选"
                elif traffic_score >=50000:
                    traffic_level = "大爆预备"
                elif traffic_score >= 10000:
                    traffic_level = "小爆一下"
                elif traffic_score >= 1000:
                    traffic_level = "有点水花"
                else:
                    traffic_level = "无人问津"
                print(f"标题：{content['title']}，流量等级：{traffic_level}")


    if choice == 4:
        if not content_list:
            print("	没数据，自己加！")
        else:
            search_term = input("请输入要搜索的标题或作者：")
            found_contents = [content for content in content_list if search_term in content["title"] or search_term in content["author"]]
            if not found_contents:
                print("未找到相关内容数据。")
            else:
                print("搜索结果如下：")
                for content in found_contents:
                    print(content)
                

                