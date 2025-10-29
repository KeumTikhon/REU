#include <iostream>
#include <vector>

// Сортировка кучей (Heap sort)
// Построение max-heap, затем извлечение максимума по одному элементу.
static void heapify(std::vector<int>& a, int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && a[left] > a[largest]) largest = left;
    if (right < n && a[right] > a[largest]) largest = right;

    if (largest != i) {
        std::swap(a[i], a[largest]);
        heapify(a, n, largest);
    }
}

static void heapSort(std::vector<int>& a) {
    int n = static_cast<int>(a.size());
    for (int i = n / 2 - 1; i >= 0; --i) heapify(a, n, i);
    for (int i = n - 1; i > 0; --i) {
        std::swap(a[0], a[i]);
        heapify(a, i, 0);
    }
}

static void printArray(const std::vector<int>& a) {
    for (int v : a) std::cout << v << ' ';
    std::cout << '\n';
}

int main() {
    std::vector<int> arr{44, 2, 39, 18, 27, 1};
    std::cout << "Исходный массив:\n";
    printArray(arr);

    heapSort(arr);

    std::cout << "Отсортированный массив (Heap Sort):\n";
    printArray(arr);
    return 0;
}