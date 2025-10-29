#include <iostream>
#include <vector>

// Пузырьковая сортировка (Bubble sort)
// Простой стабильный алгоритм: повторно проходим массив и "всплываем" большие элементы вправо.
void bubbleSort(std::vector<int>& a) {
	const int n = static_cast<int>(a.size());
	bool swapped;
	for (int i = 0; i < n - 1; ++i) {
		swapped = false;
		for (int j = 0; j < n - i - 1; ++j) {
			if (a[j] > a[j + 1]) {
				std::swap(a[j], a[j + 1]);
				swapped = true;
			}
		}
		// если за проход не было обменов — массив уже отсортирован
		if (!swapped) break;
	}
}

static void printArray(const std::vector<int>& a) {
	for (int v : a) std::cout << v << ' ';
	std::cout << '\n';
}

int main() {
	std::vector<int> arr{99, 23, 41, 6, 77, 12, 5};
	std::cout << "Исходный массив:\n";
	printArray(arr);

	bubbleSort(arr);

	std::cout << "Отсортированный массив (Bubble Sort):\n";
	printArray(arr);
	return 0;
}