N = int(input())
A_LIST = list(map(int, input().split()))

a_len = len(A_LIST)

for i in range(a_len):
    for j in range(i+1, a_len):
        if (1000 - (A_LIST[i] + A_LIST[j])) in A_LIST[j+1:]:
            print("Yes")
            import sys
            sys.exit()
print("No")