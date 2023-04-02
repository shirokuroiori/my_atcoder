T = int(input())
N = int(input())

li = [0] * (T+1)
for _ in range(N):
    L, R = map(int, input().split())
    li[L] += 1
    li[R] -= 1
r_sum = [0]
for i in range(T):
    r_sum.append(r_sum[i]+li[i])
    print(r_sum[-1])