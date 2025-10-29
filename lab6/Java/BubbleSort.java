public class BubbleSort {
    // Функция для сортировки массива методом пузырька
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        // Проходим по всем элементам массива
        for (int i = 0; i < n - 1; i++) {
            // Последний элемент на каждой итерации уже на своем месте
            for (int j = 0; j < n - i - 1; j++) {
                // Сравниваем соседние элементы
                if (arr[j] > arr[j + 1]) {
                    // Меняем местами, если они стоят в неправильном порядке
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }

    // Функция для вывода массива
    public static void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[] arr = {84, 21, 67, 3, 50, 12, 9};
        System.out.println("Исходный массив:");
        printArray(arr);

        bubbleSort(arr);

        System.out.println("Отсортированный массив:");
        printArray(arr);
    }
}