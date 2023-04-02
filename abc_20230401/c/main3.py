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
for a1 in set_a_list:
    for a2 in set_a_list:
        if X == (a1 - a2):
            ans = "Yes"
            break
print(ans)
# 2 4
# -2 -6