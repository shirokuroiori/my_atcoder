# ナップサック問題
N, W = map(int, input().split())
dp = [[0 for _ in range(W+1)] for _ in range(N+1)]

for i in range(1,N+1):
    wi, vi = map(int, input().split())

    for j in range(W+1):
        if j - wi < 0:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wi] + vi)

print(dp[-1][-1])