def sequences(k):
    def helper(i, n, out, idx):
        if n == 0:
            print(sorted(out[:idx], reverse=True))
        for j in range(i, n + 1):
            out[idx] = j
            helper(j, n - j, out, idx + 1)

    helper(1, k, [None] * k, 0)


if __name__ == '__main__':
    x = 4
    sequences(x)
