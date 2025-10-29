#include <iostream>
#include <vector>

// Бинарный поиск в отсортированном массиве
// Возвращает индекс найденного элемента или -1.
static int binarySearch(const std::vector<int>& a, int target) {
    int left = 0;
    int right = static_cast<int>(a.size()) - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (a[mid] == target) return mid;
        if (a[mid] > target) right = mid - 1;
        else left = mid + 1;
    }
    return -1;
}

static void printArray(const std::vector<int>& a) {
    for (int v : a) std::cout << v << ' ';
    std::cout << '\n';
}

int main() {
    std::vector<int> sorted{2,4,6,8,10,12,14,16,18,20};
    int target = 10;

    std::cout << "Ищем элемент " << target << " в массиве:\n";
    printArray(sorted);

    int result = binarySearch(sorted, target);
    if (result != -1) std::cout << "Элемент найден по индексу: " << result << '\n';
    else std::cout << "Элемент не найден" << '\n';
    return 0;
}