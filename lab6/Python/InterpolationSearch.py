"""Интерполяционный поиск (Interpolation Search).
Работает на равномерно распределённых отсортированных массивах.
"""


def interpolation_search(arr, lo, hi, x):
    if lo <= hi and x >= arr[lo] and x <= arr[hi]:
        # Вычисляем позицию с помощью интерполяционной формулы
        pos = lo + (((hi - lo) * (x - arr[lo])) // (arr[hi] - arr[lo]))

        # Состояние, если цель найдена
        if arr[pos] == x:
            return pos

        # Если x больше, x находится в правом подмассиве
        if arr[pos] < x:
            return interpolation_search(arr, pos + 1, hi, x)

        # Если x меньше, x находится в левом подмассиве
        if arr[pos] > x:
            return interpolation_search(arr, lo, pos - 1, x)

    return -1  # Элемент не найден


if __name__ == "__main__":
    arr = [5, 9, 12, 15, 18, 22, 27, 31, 36, 40, 45, 51, 58, 62, 70]
    x = 31
    # Печатаем массив и искомое значение
    print("Массив:", arr)
    print("Ищем элемент:", x)

    result = interpolation_search(arr, 0, len(arr) - 1, x)

    if result != -1:
        print(f"Элемент найден на позиции: {result}")
    else:
        print("Элемент не найден")