n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

d = [0] * 10000
if n == 1:
    print(arr[0])
elif n == 2:
    print(arr[0]+arr[1])
elif n == 3:
    d[0] = arr[0]
    d[1] = arr[0]+arr[1]
    d[2] = max(d[1], d[0]+arr[2], arr[1]+arr[2])
    print(d[2])
else:
    d[0] = arr[0]
    d[1] = arr[0]+arr[1]
    d[2] = max(d[1], d[0]+arr[2], arr[1]+arr[2])

    for i in range(3, n):
        d[i] = max(d[i-1], d[i-3]+arr[i-1]+arr[i], d[i-2]+arr[i])

    print(d[n-1])
