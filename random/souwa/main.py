N, K = map(int,input().split())
a_list = list(map(int, input().split()))

rum = [0]
for i in range(len(a_list)):
    rum.append(rum[i]+a_list[i])

ans = 0
for i in range(K, len(a_list)+1):
    ans += (rum[i] - rum[i-K])
print(ans)