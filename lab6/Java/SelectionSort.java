import java.util.Arrays;

public class SelectionSort {
    public static void selectionSort(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            int minIndex = i;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }
            int temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }
    }

    public static void main(String[] args) {
        int[] testArray = {95, 14, 76, 2, 39};
        System.out.println("Исходный массив: " + Arrays.toString(testArray));

        selectionSort(testArray);

        System.out.println("Отсортированный массив: " + Arrays.toString(testArray));
    }
}