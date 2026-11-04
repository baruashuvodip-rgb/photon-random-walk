def average(x_n, x_avg_old, n):
    x_avg_n = x_avg_old + (x_n - x_avg_old) / n
    return x_avg_n


def variance(x_n, x_avg_old, n):
    x_avg_n = average(x_n, x_avg_old, n)
    M2_n = (n - 1) / n * variance(x_n, x_avg_old, n - 1) + (x_n - x_avg_old) * (x_n - x_avg_n)
    std_dev_n = (M2_n / n) ** 0.5
    return std_dev_n
    