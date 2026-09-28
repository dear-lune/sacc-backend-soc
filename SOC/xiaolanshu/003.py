n = int(input()) 
#.split() 把它切成 ['0', '18', '21', '30', '20']
#[int(x) for x in ...] 把每个字符串变成数字，存进 lengths 列表
lengths = [int(x) for x in input().split()]
count = 0
for length in lengths:
    if length > 20:
        count += 1
print(count)