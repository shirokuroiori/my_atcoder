alfa = ["a", "b", "c", "d", "e", "f", "g", "h"]
gred = [[a + str(i) for a in alfa] for i in range(8, 0, -1)]

for i in range(8):
    s = input()
    if "*" in s:
        marker_num = s.split(".").index("*")
        print(gred[i][marker_num])