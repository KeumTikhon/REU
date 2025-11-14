# exponential_search.py
# Экспоненциальный поиск (Exponential Search)
#
# Идея:
# - Сначала быстро находим диапазон в котором может находиться искомый элемент,
#   увеличивая границу в геометрической прогрессии (1, 2, 4, 8, ...)
# - Затем применяем бинарный поиск в найденном интервале.
#
# Применим для отсортированных массивов. Особенно полезен, когда массив большой
# или при частичном доступе (например, поток/len неизвестен).
#
# Сложность: O(log n) (включая бинарный шаг)

from typing import List

def binary_search_in_range(arr: List[int], left: int, right: int, target: int) -> int:
    """Классический бинарный поиск в arr[left:right+1]"""
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def exponential_search(arr: List[int], target: int) -> int:
    n = len(arr)
    if n == 0:
        return -1

    # Сначала проверяем первый элемент
    if arr[0] == target:
        return 0

    # Найдем диапазон [i/2, i] такой, что arr[i] >= target
    i = 1
    while i < n and arr[i] < target:
        i *= 2

    # Выполняем бинарный поиск в диапазоне [i/2, min(i, n-1)]
    left = i // 2
    right = min(i, n - 1)
    return binary_search_in_range(arr, left, right, target)

if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 15, 20, 24, 30, 41, 50, 63, 77]
    print("Массив:", data)
    for target in [15, 2, 77, 1, 63]:
        idx = exponential_search(data, target)
        print(f"Поиск {target}: индекс {idx}")
