public class InterpolationSearch {

    public static int interpolationSearch(int[] arr, int lo, int hi, int x) {
        if (lo <= hi && x >= arr[lo] && x <= arr[hi]) {
            // Вычисляем позицию с помощью интерполяционной формулы
            int pos = lo + (((hi - lo) * (x - arr[lo])) / (arr[hi] - arr[lo]));

            // Состояние, если цель найдена
            if (arr[pos] == x) {
                return pos;
            }

            // Если x больше, x находится в правом подмассиве
            if (arr[pos] < x) {
                return interpolationSearch(arr, pos + 1, hi, x);
            }

            // Если x меньше, x находится в левом подмассиве
            if (arr[pos] > x) {
                return interpolationSearch(arr, lo, pos - 1, x);
            }
        }
        return -1;  // Элемент не найден
    }

    public static void main(String[] args) {
        int[] arr = {5, 9, 12, 15, 18, 22, 27, 31, 36, 40, 45, 51, 58, 62, 70};
        int x = 31;

        // Печатаем массив и искомое значение
        System.out.println("Массив: " + java.util.Arrays.toString(arr));
        System.out.println("Ищем элемент: " + x);

        int result = interpolationSearch(arr, 0, arr.length - 1, x);

        if (result != -1) {
            System.out.println("Элемент найден на позиции: " + result);
        } else {
            System.out.println("Элемент не найден");
        }
    }
}