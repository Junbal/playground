# 효율적인 화폐 구성
# N가지 종류의 화폐
# 화폐들의 개수를 최소한으로 이용 해서 그 가치의 합이 M원이 되도록 함.

N, M = map(int, input().split())
arr = []

for i in range(N):
    arr.append(int(input()))

d = [10001] * (10001)
for i in arr:
    d[i] = 1

for i in range(1, M+1):
    for j in arr:
        d[i] = min(d[i], d[i-j]+1)

if d[M] == 10001:
    print(-1)
else:
    print(d[M])
