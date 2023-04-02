N = int(input())
A_LIST = list(map(int, input().split()))

arari = [0, A_LIST[0]]
hazure = [0, 1 if A_LIST[0] == 0 else 0]
for i in range(1,len(A_LIST)):
    arari.append(arari[i] + A_LIST[i])
    hazure.append(hazure[i] + (1 if A_LIST[i] == 0 else 0))
Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    ans = (arari[R] - arari[L - 1]) - (hazure[R] - hazure[L - 1])
    if ans > 0:
        print("win")
    elif ans < 0:
        print("lose")
    else:
        print("draw")