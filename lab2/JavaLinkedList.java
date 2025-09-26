class Node {
    int data; // Данные которые хранит узел
    Node next; // Указатель на следующий узел

    Node(int data) {
        this.data = data; // Инициализируем данные
        this.next = null;  // Пока что следующий узел отсутствует
    }
}

public class JavaLinkedList {

    // Вывод связного списка в консоль
    public static void printList(Node head) {
        Node current = head; // Начинаем с головы
        while (current != null) { // Пока не дошли до конца списка
            System.out.print(current.data + " "); // Выводим данные текущего узла
            current = current.next; // Переходим к следующему узлу
        }
        System.out.println(); // Переводим строку
    }


    // Разворот связного списка
    public static Node reverseList(Node head) {
        Node prev = null; // Предыдущий узел
        Node current = head; // Текущий узел
        Node next = null;  // Следующий узел (временная переменная)

        while (current != null) {
            next = current.next; // Запоминаем следующий узел
            current.next = prev; // Меняем указатель текущего узла
            prev = current; // Текущий узел становится предыдущим
            current = next; // Переходим к следующему узлу
        }

        return prev; // В конце "prev" будет указывать на новую голову
    }


    // Удаление дубликатов из отсортированного связного списка
    public static void removeDuplicates(Node head) {
        if (head == null) { // Если список пуст
            return;
        }

        Node current = head;

        while (current.next != null) {
            if (current.data == current.next.data) {
                // Нашли дубликат
                current.next = current.next.next; // Вырезаем дубликат
                // Важно: Не переходим к следующему узлу
            } else {
                current = current.next; // Переходим к следующему узлу
            }
        }
    }


    public static void main(String[] args) {
        // Создаем связный список для тестирования
        Node head1 = new Node(1);
        head1.next = new Node(2);
        head1.next.next = new Node(3);
        head1.next.next.next = new Node(4);
        head1.next.next.next.next = new Node(5);

        System.out.print("Исходный список: ");
        printList(head1);

        // Разворачиваем список
        head1 = reverseList(head1);

        System.out.print("Развернутый список: ");
        printList(head1);

        // Создаем отсортированный список с дубликатами
        Node head2 = new Node(1);
        head2.next = new Node(1);
        head2.next.next = new Node(2);
        head2.next.next.next = new Node(3);
        head2.next.next.next.next = new Node(3);
        head2.next.next.next.next.next = new Node(3);
        head2.next.next.next.next.next.next = new Node(4);

        System.out.print("Исходный список с дубликатами: ");
        printList(head2);

        // Удаляем дубликаты
        removeDuplicates(head2);

        System.out.print("Список после удаления дубликатов: ");
        printList(head2);
    }
}
