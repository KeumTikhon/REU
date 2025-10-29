#include <iostream>
#include <vector>

// Быстрая сортировка (Quick sort) с использованием последнего элемента в качестве опорного
static int partition(std::vector<int>& a, int low, int high) {
    int pivot = a[high];
    int i = low - 1;
    for (int j = low; j < high; ++j) {
        if (a[j] <= pivot) {
            ++i;
            std::swap(a[i], a[j]);
        }
    }
    std::swap(a[i + 1], a[high]);
    return i + 1;
}

static void quickSort(std::vector<int>& a, int low, int high) {
    if (low < high) {
        int pi = partition(a, low, high);
        quickSort(a, low, pi - 1);
        quickSort(a, pi + 1, high);
    }
}

static void printArray(const std::vector<int>& a) {
    for (int v : a) std::cout << v << ' ';
    std::cout << '\n';
}

int main() {
    std::vector<int> array{21, 4, 18, 6, 30, 2};
    std::cout << "Исходный массив:\n";
    printArray(array);

    quickSort(array, 0, static_cast<int>(array.size()) - 1);

    std::cout << "Отсортированный массив (Quick Sort):\n";
    printArray(array);
    return 0;
}