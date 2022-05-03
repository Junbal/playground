# 숫자 카드 게임

n, m = map(int, input().split())

res = 0

for i in range(n):
    arr = list(map(int, input().split()))
    ans = min(arr)
    res = max(res, ans)

print(res)
