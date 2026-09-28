nums=list(map(int,input().split()))
target=int(input())

my_info={}
result=[]

for i,num in enumerate(nums):
    need=target-num
    if need in my_info:
        result.append([my_info[need],i])
        break
    my_info[nums[i]]=i

if result:
    print(result[0])
else:
    print("没有找到符合条件的两个数。")

