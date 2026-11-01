N = int(input("Input N: "))
arr = []
for x in range(N):
    num = int(input())
    arr.append(num)
for y in range(N):
    print(arr[N-1-y], end=" ")