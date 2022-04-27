# 개미 전사

N = int(input())
arr = list(map(int, input().split()))

dp = [0]*100
dp[0] = arr[0]
dp[1] = max(arr[0], arr[1])

for i in range(2, N):
    dp[i] = max(dp[i-1], arr[i]+dp[i-2])

print(dp[N-1])
