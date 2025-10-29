#include <iostream>
#include <vector>
#include <algorithm>

// Сортировка выбором (Selection sort)
// Идея: на каждом шаге выбираем минимальный элемент и ставим его на текущую позицию.
void selectionSort(std::vector<int>& arr) {
    const size_t n = arr.size();
    for (size_t i = 0; i < n; ++i) {
        size_t minIndex = i;
        for (size_t j = i + 1; j < n; ++j) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        if (minIndex != i) {
            std::swap(arr[i], arr[minIndex]);
        }
    }
}

static void printArray(const std::vector<int>& a) {
    for (int v : a) std::cout << v << ' ';
    std::cout << '\n';
}

int main() {
    std::vector<int> data{91, 7, 34, 58, 3};

    std::cout << "Исходный массив:\n";
    printArray(data);

    selectionSort(data);

    std::cout << "Отсортированный массив (Selection Sort):\n";
    printArray(data);

    return 0;
}