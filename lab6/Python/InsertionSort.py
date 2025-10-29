"""Сортировка вставками (Insertion Sort)."""

def insertion_sort(array):
    # Проходим по всем элементам массива, начиная со второго
    for i in range(1, len(array)):
        key = array[i]  # Текущий элемент, который нужно вставить
        j = i - 1  # Индекс предыдущего элемента

        # Перемещаем элементы array[0..i-1], которые больше key
        # на одну позицию вперед
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key  # Вставляем key на правильное место


def print_array(array):
    print(" ".join(map(str, array)))


# Основная функция для тестирования
if __name__ == "__main__":
    array = [27, 3, 45, 9, 1]

    print("Исходный массив:")
    print_array(array)

    insertion_sort(array)

    print("Отсортированный массив:")
    print_array(array)