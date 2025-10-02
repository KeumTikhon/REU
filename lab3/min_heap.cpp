#include <iostream>
#include <vector>
#include <stdexcept>

class MinHeap {
private:
    std::vector<int> heap; // Вектор для хранения элементов кучи
    
    // Возвращает индекс родительского узла
    int parent(int i) { return (i - 1) / 2; }

    // Возвращает индекс левого потомка
    int leftChild(int i) { return 2 * i + 1; }

    // Возвращает индекс правого потомка
    int rightChild(int i) { return 2 * i + 2; }
    
    // Восстановление свойства мин-кучи вверх по дереву (после вставки)
    void heapifyUp(int i) {
        while (i > 0 && heap[i] < heap[parent(i)]) {
            std::swap(heap[i], heap[parent(i)]); // Меняем местами с родителем, если нарушено свойство кучи
            i = parent(i); // Поднимаемся выше по дереву
        }
    }
    
    // Восстановление свойства мин-кучи вниз по дереву (после удаления корня)
    void heapifyDown(int i) {
        int smallest = i;
        int left = leftChild(i);
        int right = rightChild(i);
        
        // Проверка, есть ли левый потомок меньше текущего узла
        if (left < heap.size() && heap[left] < heap[smallest])
            smallest = left;
            
        // Проверка, есть ли правый потомок меньше текущего наименьшего
        if (right < heap.size() && heap[right] < heap[smallest])
            smallest = right;
        
        // Если найден потомок меньше текущего узла, меняем их местами и продолжаем вниз
        if (smallest != i) {
            std::swap(heap[i], heap[smallest]);
            heapifyDown(smallest);
        }
    }
    
public:
    // Вставка нового элемента в кучу
    void insert(int value) {
        heap.push_back(value);       // Добавляем в конец
        heapifyUp(heap.size() - 1);  // Восстанавливаем свойства кучи вверх
    }
    
    // Удаление и возврат минимального элемента (корня кучи)
    int extractMin() {
        if (heap.empty()) throw std::runtime_error("Heap is empty"); // Обработка случая пустой кучи
        
        int min = heap[0];             // Сохраняем минимальный элемент
        heap[0] = heap.back();         // Перемещаем последний элемент на место корня
        heap.pop_back();               // Удаляем последний элемент
        heapifyDown(0);                // Восстанавливаем свойства кучи вниз
        
        return min;
    }
    
    // Проверка, соблюдается ли свойство мин-кучи
    bool isMinHeap() {
        for (int i = 0; i < heap.size(); i++) {
            int left = leftChild(i);
            int right = rightChild(i);
            
            // Если левый потомок существует и он меньше родителя — нарушение
            if (left < heap.size() && heap[i] > heap[left]) return false;
            
            // То же для правого потомка
            if (right < heap.size() && heap[i] > heap[right]) return false;
        }
        return true;
    }
    
    // Печать всех элементов кучи
    void printHeap() {
        std::cout << "Heap: ";
        for (int val : heap) std::cout << val << " ";
        std::cout << std::endl;
    }
};

int main() {
    MinHeap heap;
    
    // Вставка элементов
    heap.insert(10);
    heap.insert(5);
    heap.insert(15);
    heap.insert(3);
    heap.insert(7);
    
    heap.printHeap(); // Вывод текущего состояния кучи

    std::cout << "Является ли min-кучей: " << (heap.isMinHeap() ? "да" : "нет") << std::endl;

    // Извлечение минимума
    std::cout << "Минимальный элемент: " << heap.extractMin() << std::endl;
    heap.printHeap(); // Состояние после удаления минимального элемента

    // Повторная проверка свойства кучи
    std::cout << "Является ли min-кучей: " << (heap.isMinHeap() ? "да" : "нет") << std::endl;

    return 0;
}
