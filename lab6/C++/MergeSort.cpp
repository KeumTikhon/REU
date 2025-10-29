#include <iostream>
#include <vector>

// Сортировка слиянием (Merge sort)
// Разделяй и властвуй: разбиваем на части, сортируем рекурсивно и сливаем.

static std::vector<int> merge(const std::vector<int>& left, const std::vector<int>& right) {
    std::vector<int> result;
    result.reserve(left.size() + right.size());
    size_t i = 0, j = 0;

    while (i < left.size() && j < right.size()) {
        if (left[i] < right[j]) result.push_back(left[i++]);
        else result.push_back(right[j++]);
    }
    // добавить оставшиеся элементы
    while (i < left.size()) result.push_back(left[i++]);
    while (j < right.size()) result.push_back(right[j++]);
    return result;
}

static std::vector<int> merge_sort(std::vector<int> arr) {
    if (arr.size() <= 1) return arr;
    size_t mid = arr.size() / 2;
    std::vector<int> left(arr.begin(), arr.begin() + mid);
    std::vector<int> right(arr.begin() + mid, arr.end());
    left = merge_sort(std::move(left));
    right = merge_sort(std::move(right));
    return merge(left, right);
}

static void printArray(const std::vector<int>& a) {
    for (int v : a) std::cout << v << ' ';
    std::cout << '\n';
}

int main() {
    std::vector<int> array{31, 14, 59, 2, 8, 72, 45};
    std::cout << "Исходный массив:\n";
    printArray(array);

    std::vector<int> sorted = merge_sort(array);

    std::cout << "Отсортированный массив (Merge Sort):\n";
    printArray(sorted);
    return 0;
}