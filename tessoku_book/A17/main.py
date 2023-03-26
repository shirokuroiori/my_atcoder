N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [None] * N
dp[0] = 0
dp[1] = A[0]

for i in range(2, N):
    dp[i] = min(dp[i - 1] + A[i - 1], dp[i - 2] + B[i - 2])

cnt = N-1
ans = [N]

while True:
    # print("dp[cnt]: {}, A[cnt-1]: {}, dp[cnt - 1]: {}".format(dp[cnt], A[cnt-1], dp[cnt - 1]))
    if cnt <= 1:
        break

    if dp[cnt] == A[cnt-1] + dp[cnt - 1]:
        ans.append(cnt)
        cnt -= 1
    else:
        ans.append(cnt-1)
        cnt -= 2


if ans[-1] != 1:
    ans.append(1)
ans.reverse()

print(len(ans))
print(" ".join(map(str,ans)))

# 4
# 1 2 3
# 2 4