import time

# first algorithm
def fib1(n):
    if n < 2:
        return n
    else:
        return fib1(n - 1) + fib1(n - 2)


# second algorithm
def fib2(n):
    p = 1
    j = 0
    for k in range(1, n):
        j = p + j
        p = j - p
    return j


# third algorithm
def fib3(n):
    i = 1
    j = 0
    k = 0
    h = 1
    while n > 0:
        if n % 2 != 0:
            t = j * h
            j = (i * h) + (j * k) + t
            i = (i * k) + t
        t = h ** 2
        h = (2 * k) * h + t
        k = (k ** 2) + t
        n = n // 2
    return j


for i in range(1, 40):
    t1_start = time.perf_counter()
    fib1(i)
    t1_end = time.perf_counter()
    t1 = t1_end - t1_start

    t2_start = time.perf_counter()
    fib2(i)
    t2_end = time.perf_counter()
    t2 = t1_end - t1_start

    t3_start = time.perf_counter()
    fib3(i)
    t3_end = time.perf_counter()
    t3 = t3_end - t3_start

    print(f"n={i}, fib1: {t1}, fib2:  {t2}, fib3: {t3}")