# 떡 [19, 14, 10, 17]
# 절단기 H = 15
# 자르면 [4, 0, 0, 2]
# 따라서, 손님은 6 가져 간다.
# 손님이 길이 M 을 요청할 때 적어도 M 만큼의 떡을 얻기 위해
# 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램

N, M = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = max(arr)

res = 0
while left <= right:
    total = 0
    mid = (left+right)//2
    for x in arr:
        if x > mid:
            total += x-mid
    if total < M:
        right = mid-1
    else:
        res = mid
        left = mid + 1

print(res)
