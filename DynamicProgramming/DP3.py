# 바닥 공사
# 1 X 2 -> 타일
# 2 X 1 -> 타일
# 2 X 2 -> 타일
# N X 2

N = int(input())

d = [0] * 1001
d[0] = 1
d[1] = 3

for i in range(2, N):
    d[i] = d[i-1] + 2*d[i-2]

print(d[N-1] % 796796)
