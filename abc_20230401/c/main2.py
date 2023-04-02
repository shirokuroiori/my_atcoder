N, X = map(int, input().split())
A_LIST = list(map(int, input().split()))

import sys

if X == 0:
    print("Yes")
    sys.exit()


set_a_list = set(A_LIST)
if len(set_a_list) == 1:
    print("No")
    sys.exit()

ans = "No"
import math
for a in set_a_list:
    if int(math.fabs(X - a)) in set_a_list:
        ans = "Yes"
        break
print(ans)