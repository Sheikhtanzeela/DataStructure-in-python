def knapsack(size, values, weights):
    n = len(values)
    m = [[0 for i in range(size + 1)] for i in range(n + 1)]
    for i in range(1, n):
        for j in range(size + 1):
            w = weights[i]
            v = values[i]
            if w > j:
                m[i][j] = m[i - 1][j]

            else:
                m[i][j] = max(m[i - 1][j], m[i - 1][j - w] + v)
    return m[n - 1][size]


print(knapsack(6, [10, 15, 30], [1, 2, 3]))
