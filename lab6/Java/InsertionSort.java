public class InsertionSort {

    // Метод для сортировки массива
    public static void insertionSort(int[] array) {
        // Проходим по всем элементам массива, начиная со второго
        for (int i = 1; i < array.length; i++) {
            int key = array[i]; // Текущий элемент, который нужно вставить
            int j = i - 1; // Индекс предыдущего элемента

            // Перемещаем элементы array[0..i-1], которые больше key
            // на одну позицию вперед
            while (j >= 0 && array[j] > key) {
                array[j + 1] = array[j];
                j = j - 1;
            }
            array[j + 1] = key; // Вставляем key на правильное место
        }
    }

// Метод для вывода массива
public static void printArray(int[] array) {
    for (int value : array) {
        System.out.print(value + " ");
    }
    System.out.println();
}

    // Основной метод для тестирования
    public static void main(String[] args) {
        int[] array = {23, 5, 87, 14, 62};

        System.out.println("Исходный массив:");
        printArray(array);

        insertionSort(array);

        System.out.println("Отсортированный массив:");
        printArray(array);
    }
}