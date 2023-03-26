N, S = map(int, input().split())
A = list(map(int, input().split()))

sq = [[False for _ in range(S+1)] for _ in range(N)]

sq[0][0] = True
if A[0] < S+1:
    sq[0][A[0]] = True

for i in range(1, len(sq)):
    sq[i] = sq[i - 1].copy()
    tmp = sq[i - 1].copy()

    # print("")
    # print("i:{}, A[i]:{}, sq[i]: {}".format(i, A[i], sq[i]))
    for j in range(1, S+1):
        if sq[i][j]:
            if j + A[i] <= S:
                tmp[j + A[i]] = True
        # print("j:{}, i:{}, sq[i][j]:{}, tmp:{}".format(j, i, sq[i][j], tmp))
    # sq[i][A[i]] = True
    if A[i] <= S:
        tmp[A[i]] = True
    sq[i] = tmp

# a = [i for i in range(len(sq[0]))]
# print(a)
# for i in sq:
#     tmp = []
#     for j in i:
#         if j:
#             tmp.append(1)
#         else:
#             tmp.append(0)
#     print(tmp)


if sq[-1][-1]:
    print("Yes")
else:
    print("No")