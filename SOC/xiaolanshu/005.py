def calculateScore(likes, saves,comments):
    score = likes * 2 + saves * 3+comments 
    return score

n=int(input("笔记数量(1 <= n <= 100):"))
score_list=[]
for i in range(n):
    likes, saves,comments = map(int, input().split())
    score=calculateScore(likes, saves,comments)
    score_list.append(score)
    
for i in range(len(score_list)):               #从0开始左闭右开
    for j in range(len(score_list) - 1 - i):
        if score_list[j] < score_list[j+1]:  
            score_list[j], score_list[j+1] = score_list[j+1], score_list[j]

for score in score_list:
    print(score)