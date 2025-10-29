"""Бинарный (двоичный) поиск (Binary Search).
Работает на отсортированном массиве.
"""


def binary_search(array, target):
    left = 0  # Левая граница поиска
    right = len(array) - 1  # Правая граница поиска

    while left <= right:
        # Находим середину массива
        mid = left + (right - left) // 2

        # Проверяем средний элемент
        if array[mid] == target:
            return mid  # Элемент найден

        # Если искомый элемент меньше среднего
        if array[mid] > target:
            right = mid - 1  # Перемещаемся влево
        else:
            left = mid + 1  # Перемещаемся вправо

    return -1  # Элемент не найден


def main():
    sorted_array = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    target = 14

    # Печатаем массив и искомое значение
    print("Массив:", sorted_array)
    print("Ищем элемент:", target)

    result = binary_search(sorted_array, target)

    if result != -1:
        print(f"Элемент найден на позиции: {result}")
    else:
        print("Элемент не найден")


if __name__ == "__main__":
    main()