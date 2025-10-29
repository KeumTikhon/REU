public class FibonacciSearch {

    // Функция для генерации чисел Фибоначчи
    public static int fibonacci(int n) {
        if (n <= 1)
            return n;

        int[] fib = new int[n + 2];
        fib[0] = 0;
        fib[1] = 1;
        for (int i = 2; i <= n; i++)
            fib[i] = fib[i - 1] + fib[i - 2];
        return fib[n];
    }

    // Функция поиска Фибоначчи
    public static int fibonacciSearch(int[] arr, int x) {
        int n = arr.length;

        // Находим наименьшее число Фибоначчи, большее или равное n
        int fib_m2 = 0; // (m-2)'е число Фибоначчи
        int fib_m1 = 1; // (m-1)'е число Фибоначчи
        int fib_m = fib_m2 + fib_m1;

        // Находим m такое, что F[m] >= n
        while (fib_m < n) {
            fib_m2 = fib_m1;
            fib_m1 = fib_m;
            fib_m = fib_m2 + fib_m1;
        }

        // Маркеры для элементов, которые не входят в массив
        int offset = -1;

        // Поиск
        while (fib_m > 1) {
            // Проверяем возможный индекс
            int i = Math.min(offset + fib_m2, n - 1);

            // Если x больше элемента, переходим к правому подмассиву
            if (arr[i] < x) {
                fib_m = fib_m1;
                fib_m1 = fib_m2;
                fib_m2 = fib_m - fib_m1;
                offset = i;
            }
            // Если x меньше элемента, переходим к левому подмассиву
            else if (arr[i] > x) {
                fib_m = fib_m2;
                fib_m1 = fib_m1 - fib_m2;
                fib_m2 = fib_m - fib_m1;
            }
            // Элемент найден
            else
                return i;
        }

        // Проверяем последний элемент
        if (fib_m1 == 1 && offset + 1 < n && arr[offset + 1] == x)
            return offset + 1;

        return -1; // Элемент не найден
    }

    public static void main(String[] args) {
        int[] arr = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30};
        int x = 24;

        // Печатаем массив и искомое значение
        System.out.println("Массив: " + java.util.Arrays.toString(arr));
        System.out.println("Ищем элемент: " + x);

        int result = fibonacciSearch(arr, x);

        if (result != -1)
            System.out.println("Элемент найден на позиции: " + result);
        else
            System.out.println("Элемент не найден");
    }
}