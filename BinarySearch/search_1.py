# 부품 찾기
# 부품 N개가 존재하고, 각 부품은 정수 형태의 고유한 번호가 있음.
# 손님이 M개 종류의 부품을 대량으로 구매.
# M개 종류가 다 있는지 확인.
# N = 5
# [8, 3, 7. 9. 2]
# M = 3
# [5, 7, 9]
# 있으면 yes, 없으면 no

def bs(array, target, left, right):
    while left <= right:
        mid = (left+right)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return None


n = int(input())
N = list(map(int, input().split()))
m = int(input())
M = list(map(int, input().split()))

N.sort()

for i in M:
    res = bs(N, i, 0, n-1)
    if res != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
