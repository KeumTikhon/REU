#include <iostream>
#include <vector>

// Сортировка вставками (Insertion sort)
// Идея: проходя слева направо, вставляем текущий элемент в отсортированную часть слева.
void insertionSort(std::vector<int>& a) {
    const int n = static_cast<int>(a.size());
    for (int i = 1; i < n; ++i) {
        int key = a[i];
        int j = i - 1;
        // сдвигаем элементы, большие ключа, вправо
        while (j >= 0 && a[j] > key) {
            a[j + 1] = a[j];
            --j;
        }
        a[j + 1] = key;
    }
}

static void printArray(const std::vector<int>& a) {
    for (int v : a) std::cout << v << ' ';
    std::cout << '\n';
}

int main() {
    std::vector<int> arr{20, 3, 15, 9, 27};
    std::cout << "Исходный массив:\n";
    printArray(arr);

    insertionSort(arr);

    std::cout << "Отсортированный массив (Insertion Sort):\n";
    printArray(arr);
    return 0;
}