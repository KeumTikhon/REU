import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class ListSplit {
    public static void main(String[] args) {
        List<String> list_1 = new ArrayList<>();
        list_1.add("a");
        list_1.add("1");
        list_1.add("b");
        list_1.add("2");
        list_1.add("c");
        list_1.add("3");

        List<String> letters = new ArrayList<>();
        List<String> numbers = new ArrayList<>();

        Stack<String> letterStack = new Stack<>();
        Stack<String> numberStack = new Stack<>();

        for (String item : list_1) {
            if (item.matches("\\d+")) { // Проверяем, состоит ли строка только из цифр
                numberStack.push(item);
            } else {
                letterStack.push(item);
            }
        }
         // Извлекаем элементы из стеков
        while (!letterStack.isEmpty()) {
            letters.add(letterStack.pop());
        }

        while (!numberStack.isEmpty()) {
            numbers.add(numberStack.pop());
        }

        System.out.println("Буквы: " + letters);
        System.out.println("Числа: " + numbers);


    }
}
