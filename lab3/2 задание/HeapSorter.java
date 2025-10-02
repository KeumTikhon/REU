import java.util.Arrays;

public class HeapSorter {

    // Преобразование массива в max-кучу
    public static void buildMaxHeap(int[] arr) {
        int n = arr.length;

        // Начинаем с последнего внутреннего узла и идём вверх
        for (int i = n / 2 - 1; i >= 0; i--)
            heapify(arr, n, i);
    }

    // Пирамидальная сортировка
    public static void heapSort(int[] arr) {
        int n = arr.length;

        // Шаг 1: Построение max-кучи
        buildMaxHeap(arr);

        // Шаг 2: Последовательно "выталкиваем" максимумы в конец массива
        for (int i = n - 1; i > 0; i--) {
            // Меняем корень с последним элементом
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;

            // Восстанавливаем свойства кучи для оставшегося массива
            heapify(arr, i, 0);
        }
    }

    // Восстановление max-кучи для поддерева с корнем в i
    private static void heapify(int[] arr, int n, int i) {
        int largest = i;             // Изначально предполагаем, что корень — наибольший
        int left = 2 * i + 1;        // Левый потомок
        int right = 2 * i + 2;       // Правый потомок

        // Если левый потомок больше текущего наибольшего
        if (left < n && arr[left] > arr[largest])
            largest = left;

        // Если правый потомок больше текущего наибольшего
        if (right < n && arr[right] > arr[largest])
            largest = right;

        // Если наибольший элемент — не корень, меняем местами и продолжаем рекурсивно
        if (largest != i) {
            int swap = arr[i];
            arr[i] = arr[largest];
            arr[largest] = swap;

            heapify(arr, n, largest);
        }
    }

    public static void main(String[] args) {
        int[] arr = {12, 11, 13, 5, 6, 7};

        // Исходный массив
        System.out.println("Исходный массив: " + Arrays.toString(arr));

        // Построение max-кучи
        buildMaxHeap(arr);
        System.out.println("После построения max-кучи: " + Arrays.toString(arr));

        // Пирамидальная сортировка
        heapSort(arr);
        System.out.println("После пирамидальной сортировки: " + Arrays.toString(arr));
    }
}
