# https://cses.fi/problemset/task/2217

def collecting_numbers(n, arr):
    xx = [0]*(n+1)
    for i in range(n):
        xx[arr[i]] = i

    ans, last = 1, 0
    for i in range(1, n+1):
        if last > xx[i]:
            ans += 1
        last = xx[i]
    print(ans)

n, m = map(int, input().split(' '))
arr = [int(x) for x in input().split(' ')]
for i in range(m):
    a, b = map(int, input().split(' '))
    arr[a-1] , arr[b-1] = arr[b-1], arr[a-1]
    collecting_numbers(n, arr)