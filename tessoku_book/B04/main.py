N_str = input()
n_len = len(N_str)

n_sum = 0
for i, n in enumerate(N_str[::-1]):
    n_sum += (int(n) * (2**i))
print(n_sum)