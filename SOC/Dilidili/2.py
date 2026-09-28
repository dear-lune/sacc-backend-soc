daily_views = []  
print("请输入7天的播放量数据：")
for i in range(7):
    views = int(input(f"请输入第 {i+1} 天的播放量: "))
    daily_views.append(views) 
total_views = 0  
total_views = sum(daily_views)
print(f"累计播放量: {total_views}")