#include <iostream>
#include <vector>

// Поиск Фибоначчи (Fibonacci Search)
// Использует числа Фибоначчи для деления диапазона поиска
static int fibonacciSearch(const std::vector<int>& arr, int x) {
	int n = static_cast<int>(arr.size());
	int fib_m2 = 0; // (m-2)th Fibonacci
	int fib_m1 = 1; // (m-1)th Fibonacci
	int fib_m = fib_m2 + fib_m1; // mth Fibonacci

	while (fib_m < n) {
		fib_m2 = fib_m1;
		fib_m1 = fib_m;
		fib_m = fib_m2 + fib_m1;
	}

	int offset = -1;
	while (fib_m > 1) {
		int i = std::min(offset + fib_m2, n - 1);
		if (arr[i] < x) {
			fib_m = fib_m1;
			fib_m1 = fib_m2;
			fib_m2 = fib_m - fib_m1;
			offset = i;
		} else if (arr[i] > x) {
			fib_m = fib_m2;
			fib_m1 = fib_m1 - fib_m2;
			fib_m2 = fib_m - fib_m1;
		} else return i;
	}

	if (fib_m1 && offset + 1 < n && arr[offset + 1] == x) return offset + 1;
	return -1;
}

static void printArray(const std::vector<int>& a) {
	for (int v : a) std::cout << v << ' ';
	std::cout << '\n';
}

int main() {
	std::vector<int> arr{11,24,33,47,59,62,77,83,88,92,105};
	int x = 83;

	std::cout << "Ищем элемент " << x << " в массиве:\n";
	printArray(arr);

	int result = fibonacciSearch(arr, x);
	if (result != -1) std::cout << "Элемент найден по индексу: " << result << '\n';
	else std::cout << "Элемент не найден" << '\n';
	return 0;
}