public class ShellSort {

    // Функция для сортировки Шелла
    public static void shellSort(int[] arr) {
        int n = arr.length;

        // Начинаем с большого промежутка и уменьшаем его
        for (int gap = n / 2; gap > 0; gap /= 2) {
            // Проходим по всем элементам с текущим промежутком
            for (int i = gap; i < n; i++) {
                // Сохраняем текущий элемент
                int temp = arr[i];
                int j;

                // Сдвигаем элементы, которые больше temp, вправо
                for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
                    arr[j] = arr[j - gap];
                }

                // Вставляем temp на правильное место
                arr[j] = temp;
            }
        }
    }

    // Функция для вывода массива
    public static void printArray(int[] arr) {
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        // Пример использования
        int[] arr = {14, 55, 6, 23, 7};

        System.out.print("Исходный массив: ");
        printArray(arr);

        shellSort(arr);

        System.out.print("Отсортированный массив: ");
        printArray(arr);
    }
}