public class QuickSort {
    // Основной метод для запуска сортировки
    public static void main(String[] args) {
        int[] array = {31, 7, 88, 12, 5, 47};

        System.out.println("Исходный массив:");
        printArray(array);

        quickSort(array, 0, array.length - 1);

        System.out.println("\nОтсортированный массив:");
        printArray(array);
    }
    // Метод для сортировки массива
    public static void quickSort(int[] array, int low, int high) {
        if (low < high) {
            // pi - это индекс разбиения, array[pi] находится на своем месте
            int pi = partition(array, low, high);

            // Отсортировать элементы до и после разбиения
            quickSort(array, low, pi - 1);
            quickSort(array, pi + 1, high);
        }
    }
    // Метод для разбиения массива
    private static int partition(int[] array, int low, int high) {
        // Выбираем последний элемент в качестве опорного
        int pivot = array[high];
        int i = (low - 1); // Индекс меньшего элемента

        for (int j = low; j < high; j++) {
            // Если текущий элемент меньше или равен опорному
            if (array[j] <= pivot) {
                i++;

                // Поменять местами array[i] и array[j]
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }

        // Поменять местами array[i+1] и array[high] (опорный элемент)
        int temp = array[i + 1];
        array[i + 1] = array[high];
        array[high] = temp;

        return i + 1;
    }
    // Вспомогательный метод для вывода массива
    private static void printArray(int[] array) {
        for (int value : array) {
            System.out.print(value + " ");
        }
        System.out.println();
    }
}
