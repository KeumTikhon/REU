import java.util.Arrays;

public class BinarySearch {
    // Метод для выполнения бинарного поиска
    public static int binarySearch(int[] array, int target) {
        int left = 0; // Левая граница поиска
        int right = array.length - 1; // Правая граница поиска

        while (left <= right) {
            // Находим середину массива
            int mid = left + (right - left) / 2;
            // Проверяем средний элемент
            if (array[mid] == target) {
                return mid; // Элемент найден
            }

            // Если искомый элемент меньше среднего
            if (array[mid] > target) {
                right = mid - 1; // Перемещаемся влево
            } else {
                left = mid + 1; // Перемещаемся вправо
            }
        }
        return -1; // Элемент не найден
    }
    public static void main(String[] args) {
        int[] sortedArray = {2, 6, 8, 11, 14, 17, 19, 23, 29, 31};
        int target = 14;

        // Печатаем массив и искомое значение
        System.out.println("Массив: " + Arrays.toString(sortedArray));
        System.out.println("Ищем элемент: " + target);

        int result = binarySearch(sortedArray, target);

        if (result != -1) {
            System.out.println("Элемент найден на позиции: " + result);
        } else {
            System.out.println("Элемент не найден");
        }
    }
}
