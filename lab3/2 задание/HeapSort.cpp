#include <iostream>
#include <vector>

class HeapSorter {
private:
    // Преобразует поддерево с корнем в i в max-кучу
    static void heapify(std::vector<int>& arr, int n, int i) {
        int largest = i;           // Изначально считаем корень наибольшим
        int left = 2 * i + 1;      // Левый потомок
        int right = 2 * i + 2;     // Правый потомок

        // Если левый потомок больше текущего наибольшего — обновляем
        if (left < n && arr[left] > arr[largest])
            largest = left;

        // То же для правого потомка
        if (right < n && arr[right] > arr[largest])
            largest = right;

        // Если наибольший элемент — не корень, меняем и продолжаем рекурсивно
        if (largest != i) {
            std::swap(arr[i], arr[largest]);
            heapify(arr, n, largest);
        }
    }

public:
    // Построение max-кучи из массива
    static void buildMaxHeap(std::vector<int>& arr) {
        int n = arr.size();
        // Начинаем с последнего внутреннего узла
        for (int i = n / 2 - 1; i >= 0; i--)
            heapify(arr, n, i);
    }

    // Пирамидальная сортировка (heap sort)
    static void heapSort(std::vector<int>& arr) {
        int n = arr.size();

        // Шаг 1: строим max-кучу
        buildMaxHeap(arr);

        // Шаг 2: извлекаем элементы из кучи по одному
        for (int i = n - 1; i > 0; i--) {
            std::swap(arr[0], arr[i]); // Перемещаем текущий максимум в конец
            heapify(arr, i, 0);        // Восстанавливаем кучу на оставшейся части
        }
    }

    // Печать содержимого массива
    static void printArray(const std::vector<int>& arr) {
        for (int val : arr) std::cout << val << " ";
        std::cout << std::endl;
    }
};

int main() {
    std::vector<int> arr = {12, 11, 13, 5, 6, 7};

    std::cout << "Исходный массив: ";
    HeapSorter::printArray(arr);

    // Построение max-кучи
    HeapSorter::buildMaxHeap(arr);
    std::cout << "После построения max-кучи: ";
    HeapSorter::printArray(arr);

    // Выполнение сортировки
    HeapSorter::heapSort(arr);
    std::cout << "После пирамидальной сортировки: ";
    HeapSorter::printArray(arr);

    return 0;
}
