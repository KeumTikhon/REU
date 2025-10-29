def selection_sort(arr):
    """Сортировка выбором (Selection Sort).
    Проходим по массиву, для каждой позиции находим минимальный элемент
    и ставим его на текущую позицию.
    """
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]


def print_array(arr):
    print(" ".join(map(str, arr)))


if __name__ == "__main__":
    test_array = [31, 4, 77, 2, 19]
    print("Исходный массив:")
    print_array(test_array)

    selection_sort(test_array)

    print("Отсортированный массив:")
    print_array(test_array)