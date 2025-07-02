import math
import time

import psutil


def gcd(N):

    if N % 2 == 0:
        A = B = N // 2
    else:
        # Находим наибольший делитель d < N
        d = 1
        for i in range(2, int(math.isqrt(N)) + 1):
            if N % i == 0:
                d = max(d, i, N // i)
        A = d
        B = N - d

    print(A, B)


if __name__ == "__main__":
    N = int(input())
    start_time = time.time()

    process = psutil.Process()
    start_memory = process.memory_info().rss

    # выполнение функции
    gcd(N)

    end_time = time.time()
    execution_time = end_time - start_time

    end_memory = process.memory_info().rss
    memory_usage = (end_memory - start_memory) / (1024 * 1024)  # Convert to MB
    print("Время выполнения: {:.6f} сек".format(execution_time))
    print("Использовано памяти: {:.3f} МБ".format(max(0, memory_usage)))

print("Щербина К.А. 090301-ПОВа-з23")
