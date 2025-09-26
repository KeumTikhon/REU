#include <iostream>

// Определение структуры узла связного списка
struct Node {
    int data;
    Node* next;

    Node(int data) : data(data), next(nullptr) {}
};

// Функция для вывода связного списка (для тестирования)
void printList(Node* head) {
    Node* current = head;
    while (current != nullptr) {
        std::cout << current->data << " ";
        current = current->next;
    }
    std::cout << std::endl;
}


// **Задание 1: Разворот связного списка**
Node* reverseList(Node* head) {
    Node* prev = nullptr;  // Предыдущий узел (изначально null)
    Node* current = head;   // Текущий узел (начинаем с головы)
    Node* next = nullptr;    // Следующий узел

    while (current != nullptr) {
        // 1. Сохраняем указатель на следующий узел
        next = current->next;

        // 2. Меняем указатель текущего узла, чтобы он указывал на предыдущий
        current->next = prev;

        // 3. Сдвигаем указатели prev и current на один шаг вперед
        prev = current;
        current = next;
    }

    // После завершения цикла prev будет указывать на новую голову развернутого списка
    return prev;
}





// **Задание 2: Удаление дубликатов из отсортированного связного списка**
void removeDuplicates(Node* head) {
    if (head == nullptr) {
        return; // Пустой список - ничего делать не нужно
    }

    Node* current = head;

    while (current->next != nullptr) {
        if (current->data == current->next->data) {
            // Нашли дубликат
            Node* duplicate = current->next; // Узел, который нужно удалить
            current->next = current->next->next; // Перенаправляем указатель current, чтобы пропустить дубликат
            delete duplicate; // Освобождаем память, занимаемую дубликатом
        } else {
            // Дубликата нет, переходим к следующему узлу
            current = current->next;
        }
    }
}



int main() {
    // Создаем связный список для тестирования
    Node* head1 = new Node(1);
    head1->next = new Node(2);
    head1->next->next = new Node(3);
    head1->next->next->next = new Node(4);
    head1->next->next->next->next = new Node(5);

    std::cout << "Исходный список: ";
    printList(head1);

    // Разворачиваем список
    head1 = reverseList(head1);

    std::cout << "Развернутый список: ";
    printList(head1);


    // Создаем отсортированный список с дубликатами для тестирования
    Node* head2 = new Node(1);
    head2->next = new Node(1);
    head2->next->next = new Node(2);
    head2->next->next->next = new Node(3);
    head2->next->next->next->next = new Node(3);
    head2->next->next->next->next->next = new Node(3);
    head2->next->next->next->next->next->next = new Node(4);

    std::cout << "Исходный список с дубликатами: ";
    printList(head2);

    // Удаляем дубликаты
    removeDuplicates(head2);

    std::cout << "Список после удаления дубликатов: ";
    printList(head2);


    // Освобождаем память
    // (Для простоты примера, не освобождаю память полностью после разворота.  В реальном коде нужно пройтись по списку и удалить все узлы.)
    Node* current = head2;
    while (current != nullptr) {
        Node* next = current->next;
        delete current;
        current = next;
    }

    return 0;
}