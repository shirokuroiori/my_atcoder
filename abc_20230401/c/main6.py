n,x = map(int,input().split())
s = list(map(int,input().split()))
ans = 0
s = set(s)
tar = 0
for i in s:
    tar = i + x
    print("tar: {}, i: {}, x: {}".format(tar, i ,x))
    if tar in s:
        ans = 1
        break
    else:
        ans = 0
if ans:
    print('Yes')
else:
    print("No")