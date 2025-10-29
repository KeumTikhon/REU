#include <iostream>
#include <vector>

// Сортировка Шелла (Shell sort)
// Улучшение вставок: используем уменьшение шага (gap) для предварительной сортировки подпоследовательностей.
void shellSort(std::vector<int>& arr) {
	int n = static_cast<int>(arr.size());
	for (int gap = n / 2; gap > 0; gap /= 2) {
		for (int i = gap; i < n; ++i) {
			int temp = arr[i];
			int j = i;
			while (j >= gap && arr[j - gap] > temp) {
				arr[j] = arr[j - gap];
				j -= gap;
			}
			arr[j] = temp;
		}
	}
}

static void printArray(const std::vector<int>& a) {
	for (int v : a) std::cout << v << ' ';
	std::cout << '\n';
}

int main() {
	std::vector<int> arr{17, 29, 8, 46, 1};
	std::cout << "Исходный массив:\n";
	printArray(arr);

	shellSort(arr);

	std::cout << "Отсортированный массив (Shell Sort):\n";
	printArray(arr);
	return 0;
}
