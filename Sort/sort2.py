# 위에서 아래로
# 입력받은 수열을 내림차순으로 정렬하라

N = int(input())

arr = []
for i in range(N):
    arr.append(int(input()))

arr.sort(reverse=True)

for i in arr:
    print(i, end=" ")
