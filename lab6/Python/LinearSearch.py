"""Линейный (последовательный) поиск (Linear Search).
"""


def linear_search(arr, target):
    # Проходим по всем элементам массива
    for i in range(len(arr)):
        # Если нашли искомый элемент
        if arr[i] == target:
            return i  # Возвращаем индекс найденного элемента
    return -1  # Возвращаем -1, если элемент не найден


def main():
    array = [14, 6, 9, 2, 33, 7, 18]
    target = 33  # Искомое значение (существует в массиве)

    # Печатаем массив и искомое значение
    print("Массив:", array)
    print("Ищем элемент:", target)

    # Вызываем функцию поиска
    result = linear_search(array, target)

    # Выводим результат
    if result != -1:
        print(f"Элемент найден на позиции: {result}")
    else:
        print("Элемент не найден")


if __name__ == "__main__":
    main()