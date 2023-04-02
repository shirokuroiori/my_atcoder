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
    if a > 0:
        if int((X - a)* -1) in set_a_list:
            ans = "Yes1"
            break
    else:
        if int(X - (a * -1)) in set_a_list:
            ans = "Yes2"
            break

print(ans)
# 4 5
# 1 2 3 4