#성적이 낮은 순서로 학생 출력하기
# 2
# jenny 80
# denis 90

N = int(input())
arr = []

for i in range(N):
    data = input().split()
    data[1] = int(data[1])
    arr.append([data[0], data[1]])

arr = sorted(arr, key=lambda student: student[1])

for i in arr:
    print(i[0], end=' ')
