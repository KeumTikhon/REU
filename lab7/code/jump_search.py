# jump_search.py
# Поиск скачками (Jump Search)
#
# Цель:
# - Поиск в отсортированном массиве путём "прыжков" фиксированной длины, затем линейный поиск внутри блокa.
#
# Характеристики:
# - Хорош для массивов, где чтение элементов быстрый доступ и данные отсортированы.
# - Оптимальный шаг m ≈ sqrt(n) => сложность O(√n)
#
# Временная сложность: O(√n)
# Пространственная: O(1)

from typing import List
import math

def jump_search(arr: List[int], target: int) -> int:
    """
    Возвращает индекс target в отсортированном arr или -1, если не найден.
    """
    n = len(arr)
    if n == 0:
        return -1

    # Размер шага: обычно sqrt(n)
    step = int(math.sqrt(n))
    prev = 0

    # Делаем прыжки, пока элемент в правой границе блока меньше target
    while prev < n and arr[min(n - 1, prev + step - 1)] < target:
        prev += step
        # Если вышли за пределы массива — not found
        if prev >= n:
            return -1

    # Теперь выполняем линейный поиск в блоке от prev до min(prev+step-1, n-1)
    end = min(n, prev + step)
    for i in range(prev, end):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    data = sorted([2, 3, 7, 12, 19, 23, 27, 31, 36, 40, 45, 49])
    print("Массив:", data)
    targets = [23, 5, 49, 2]
    for t in targets:
        idx = jump_search(data, t)
        print(f"Поиск {t}: индекс {idx}")
