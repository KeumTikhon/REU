#include <iostream>
#include <vector>

// Линейный (последовательный) поиск
// Возвращает индекс первого вхождения или -1 если не найдено.
static int linearSearch(const std::vector<int>& a, int target) {
	for (size_t i = 0; i < a.size(); ++i) {
		if (a[i] == target) return static_cast<int>(i);
	}
	return -1;
}

static void printArray(const std::vector<int>& a) {
	for (int v : a) std::cout << v << ' ';
	std::cout << '\n';
}

int main() {
	std::vector<int> arr{2, 8, 5, 11, 6, 14, 3};
	int target = 11;

	std::cout << "Ищем элемент " << target << " в массиве:\n";
	printArray(arr);

	int result = linearSearch(arr, target);
	if (result != -1) std::cout << "Элемент найден по индексу: " << result << '\n';
	else std::cout << "Элемент не найден" << '\n';

	return 0;
}
