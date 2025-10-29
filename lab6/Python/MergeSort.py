"""Сортировка слиянием (Merge Sort).
Рекурсивная реализация слиянием.
"""


def merge_sort(arr):
    # Базовый случай: массив длиной 0 или 1 уже отсортирован
    if len(arr) <= 1:
        return arr

    # Находим середину массива
    mid = len(arr) // 2

    # Делим массив на две части
    left = arr[:mid]
    right = arr[mid:]

    # Рекурсивно сортируем каждую часть
    left = merge_sort(left)
    right = merge_sort(right)

    # Сливаем отсортированные части
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    # Пока есть элементы в обоих массивах
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Добавляем оставшиеся элементы
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def print_array(arr):
    print(" ".join(map(str, arr)))


if __name__ == "__main__":
    array = [91, 7, 34, 58, 3, 66, 27]
    print("Исходный массив:")
    print_array(array)

    sorted_array = merge_sort(array)

    print("Отсортированный массив:")
    print_array(sorted_array)