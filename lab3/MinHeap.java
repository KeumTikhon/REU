import java.util.ArrayList;
import java.util.List;

public class MinHeap {
    private List<Integer> heap;

    public MinHeap() {
        heap = new ArrayList<>();
    }

    // Индекс родительского узла
    private int parent(int i) { return (i - 1) / 2; }

    // Индекс левого потомка
    private int leftChild(int i) { return 2 * i + 1; }

    // Индекс правого потомка
    private int rightChild(int i) { return 2 * i + 2; }

    // Восстановление свойств кучи вверх по дереву после вставки
    private void heapifyUp(int i) {
        while (i > 0 && heap.get(i) < heap.get(parent(i))) {
            swap(i, parent(i)); // Обмен с родителем
            i = parent(i);      // Переход вверх
        }
    }

    // Восстановление свойств кучи вниз по дереву после удаления
    private void heapifyDown(int i) {
        int smallest = i;
        int left = leftChild(i);
        int right = rightChild(i);

        // Проверка, есть ли левый потомок меньше текущего узла
        if (left < heap.size() && heap.get(left) < heap.get(smallest))
            smallest = left;

        // Проверка правого потомка
        if (right < heap.size() && heap.get(right) < heap.get(smallest))
            smallest = right;

        // Если найден меньший потомок, меняем и продолжаем вниз
        if (smallest != i) {
            swap(i, smallest);
            heapifyDown(smallest);
        }
    }

    // Обмен значений в куче
    private void swap(int i, int j) {
        int temp = heap.get(i);
        heap.set(i, heap.get(j));
        heap.set(j, temp);
    }

    // Вставка элемента в кучу
    public void insert(int value) {
        heap.add(value);
        heapifyUp(heap.size() - 1);
    }

    // Удаление и возврат минимального элемента
    public int extractMin() {
        if (heap.isEmpty()) throw new IllegalStateException("Куча пуста");

        int min = heap.get(0); // Корень кучи — минимум
        heap.set(0, heap.get(heap.size() - 1)); // Перемещаем последний элемент на место корня
        heap.remove(heap.size() - 1); // Удаляем последний элемент
        heapifyDown(0); // Восстанавливаем структуру

        return min;
    }

    // Проверка: соблюдается ли свойство мин-кучи
    public boolean isMinHeap() {
        for (int i = 0; i < heap.size(); i++) {
            int left = leftChild(i);
            int right = rightChild(i);

            if (left < heap.size() && heap.get(i) > heap.get(left)) return false;
            if (right < heap.size() && heap.get(i) > heap.get(right)) return false;
        }
        return true;
    }

    // Печать содержимого кучи
    public void printHeap() {
        System.out.print("Куча: ");
        for (int val : heap) System.out.print(val + " ");
        System.out.println();
    }

    // Основной метод: демонстрация работы
    public static void main(String[] args) {
        MinHeap heap = new MinHeap();

        // Вставка элементов
        heap.insert(10);
        heap.insert(5);
        heap.insert(15);
        heap.insert(3);
        heap.insert(7);

        heap.printHeap();
        System.out.println("Является ли min-кучей: " + (heap.isMinHeap() ? "да" : "нет"));

        // Извлечение минимального элемента
        System.out.println("Минимальный элемент: " + heap.extractMin());
        heap.printHeap();

        // Повторная проверка
        System.out.println("Является ли min-кучей: " + (heap.isMinHeap() ? "да" : "нет"));
    }
}
