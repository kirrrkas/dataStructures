import time
import psutil
import numpy as np


def linear():
    n = 200
    A = np.random.rand(n, n).astype(np.float32)
    B = np.random.rand(n, n).astype(np.float32)

    start = time.time()
    C = np.zeros((n, n), dtype=np.float32)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i, j] += A[i, k] * B[k, j]
    end = time.time()

    t_linear = end - start
    flops_linear = (2 * n ** 3) / (t_linear * 10**6)

    print("Время: ", t_linear, ". Производительность, MFLOPS: ", flops_linear)


def np_blas():
    # Размер матрицы
    n = 2048

    # Генерация случайных матриц типа float32 (для лучшей производительности)
    A = np.random.rand(n, n).astype(np.float32)
    B = np.random.rand(n, n).astype(np.float32)

    # Замер времени
    start = time.time()
    C_numpy = np.dot(A, B)  # или A @ B (эквивалентно)
    end = time.time()

    # Вычисление производительности
    t_numpy = end - start
    flops_numpy = (2 * n**3) / (t_numpy * 10**6)  # MFLOPS

    print(f"Время NumPy (BLAS): {t_numpy:.3f} сек")
    print(f"Производительность NumPy (BLAS): {flops_numpy:.2f} MFLOPS")


if __name__ == "__main__":
    start_time = time.time()

    process = psutil.Process()
    start_memory = process.memory_info().rss

    # выполнение функции
    #linear()
    #np_blas()

    end_time = time.time()
    execution_time = end_time - start_time

    end_memory = process.memory_info().rss
    memory_usage = (end_memory - start_memory) / (1024 * 1024)  # Convert to MB
    print("Время выполнения: {:.6f} сек".format(execution_time))
    print("Использовано памяти: {:.3f} МБ".format(max(0, memory_usage)))

print("Щербина К.А. 090301-ПОВа-з23")
