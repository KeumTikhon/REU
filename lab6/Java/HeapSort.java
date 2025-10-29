import java.util.Arrays;

public class HeapSort {

    public static void heapify(int[] arr, int n, int i) {
        int largest = i;  // Инициализируем наибольший элемент как корень
        int left = 2 * i + 1;  // левый = 2*i + 1
        int right = 2 * i + 2;  // правый = 2*i + 2

        // Проверяем существует ли левый дочерний элемент больший, чем корень
        if (left < n && arr[i] < arr[left]) {
            largest = left;
        }

        // Проверяем существует ли правый дочерний элемент больший, чем корень
        if (right < n && arr[largest] < arr[right]) {
            largest = right;
        }

        // Меняем корень, если нужно
        if (largest != i) {
            int temp = arr[i];
            arr[i] = arr[largest];
            arr[largest] = temp;
            // Рекурсивно применяем heapify к затронутому поддереву
            heapify(arr, n, largest);
        }
    }

    public static void heapSort(int[] arr) {
        int n = arr.length;
        // Построение max-heap.
        for (int i = n / 2 - 1; i >= 0; i--) {
            heapify(arr, n, i);
        }

        // Один за другим извлекаем элементы
        for (int i = n - 1; i > 0; i--) {
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;
            heapify(arr, i, 0);
        }
    }

    // Пример использования:
    public static void main(String[] args) {
        int[] arr = {71, 13, 6, 20, 4, 89};
        System.out.println("Исходный массив: " + Arrays.toString(arr));

        heapSort(arr);

        System.out.println("Отсортированный массив: " + Arrays.toString(arr));
    }
}