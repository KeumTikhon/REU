#include <iostream>

// Интерполяционный поиск в отсортированном массиве
// Возвращает индекс найденного элемента или -1, если не найден.
int interpolationSearch(int arr[], int lo, int hi, int x) {
    if (lo <= hi && x >= arr[lo] && x <= arr[hi]) {
        // Вычисляем оценочную позицию методом интерполяции
        int pos = lo + (((hi - lo) * (x - arr[lo])) / (arr[hi] - arr[lo]));

        // Если элемент найден в оценочной позиции — вернём индекс
        if (arr[pos] == x) {
            return pos;
        }

        // Иначе рекурсивно ищем в левом или правом поддиапазоне
        if (arr[pos] < x) {
            return interpolationSearch(arr, pos + 1, hi, x);
        }

        if (arr[pos] > x) {
            return interpolationSearch(arr, lo, pos - 1, x);
        }
    }
    return -1;  // Элемент не найден
}

int main() {
    int arr[] = { 5, 9, 14, 17, 23, 28, 31, 36, 40, 44, 50, 61, 73, 85, 97 };
    int n = sizeof(arr) / sizeof(arr[0]);
    int x = 36;

    int result = interpolationSearch(arr, 0, n - 1, x);

    if (result != -1) {
        std::cout << "Элемент найден по индексу: " << result << std::endl;
    }
    else {
        std::cout << "Элемент не найден" << std::endl;
    }

    return 0;
}