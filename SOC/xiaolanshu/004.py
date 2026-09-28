def calculateScore(likes, saves):
    score = likes * 2 + saves * 3
    return score
likes, saves = map(int, input().split())   #map批量处理
result = calculateScore(likes, saves)
print(result)