#두 배열의 원소 교체
# A와 B 배열이 있으면, K번 A와 B의 값 교체를 이용하여
# sum(A)를 최댓값으로 만들어라

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B, reverse=True)

for i in range(N):
    if K == 0:
        break
    for j in range(N):
        if A[j] < B[i]:
            A[j], B[i] = B[i], A[j]
            K-=1
            break

print(sum(A)) 
