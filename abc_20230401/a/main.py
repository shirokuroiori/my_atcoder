N = int(input())
S = input()

ans = "Yes"
if len(S) > 1:
    for i in range(1,len(S)):
        if S[i] == S[i - 1]:
            ans = "No"
            break
print(ans)