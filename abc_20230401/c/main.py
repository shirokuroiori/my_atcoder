N, X = map(int, input().split())
A_LIST = list(map(int, input().split()))

if X == 0:
    print("Yes")
    import sys
    sys.exit()

ans = "No"
import math
for a in A_LIST:
    if int(math.fabs(X - a)) in A_LIST:
        ans = "Yes"
        break
print(ans)