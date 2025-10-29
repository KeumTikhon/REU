import java.util.Arrays;

public class LinearSearch {

    // Функция линейного поиска
    public static int linearSearch(int[] arr, int target) {
        // Проходим по всем элементам массива
        for (int i = 0; i < arr.length; i++) {
            // Если нашли искомый элемент
            if (arr[i] == target) {
                return i; // Возвращаем индекс найденного элемента
            }
        }
        return -1; // Возвращаем -1, если элемент не найден
    }

    public static void main(String[] args) {
        // Создаем массив
        int[] array = {14, 6, 9, 2, 33, 7, 18};
        int target = 33; // Искомое значение

        // Печатаем массив и искомое значение
        System.out.println("Массив: " + Arrays.toString(array));
        System.out.println("Ищем элемент: " + target);

        // Вызываем функцию поиска
        int result = linearSearch(array, target);

        // Выводим результат
        if (result != -1) {
            System.out.println("Элемент найден на позиции: " + result);
        } else {
            System.out.println("Элемент не найден");
        }
    }
}