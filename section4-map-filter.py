def times2(x):
    return x*2

seq = [1, 2, 3, 4, 5]

new_seq = list(map(times2, seq))

print(new_seq)