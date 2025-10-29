"""Пирамидальная сортировка (Heap Sort).
Heapify и heap_sort с русскими комментариями.
"""


def heapify(arr, n, i):
    largest = i  # Инициализируем наибольший элемент как корень
    left = 2 * i + 1  # левый = 2*i + 1
    right = 2 * i + 2  # правый = 2*i + 2

    # Проверяем существует ли левый дочерний элемент больший, чем корень
    if left < n and arr[i] < arr[left]:
        largest = left

    # Проверяем существует ли правый дочерний элемент больший, чем корень
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Меняем корень, если нужно
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # своп
        # Рекурсивно применяем heapify к затронутому поддереву
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    # Построение max-heap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Один за другим извлекаем элементы
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # меняем корень с последним элементом
        heapify(arr, i, 0)


def print_array(arr):
    print(" ".join(map(str, arr)))


if __name__ == "__main__":
    arr = [72, 11, 5, 19, 3, 88]
    print("Исходный массив:")
    print_array(arr)

    heap_sort(arr)

    print("Отсортированный массив:")
    print_array(arr)