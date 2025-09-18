import java.util.Stack;

public class StringSplit {
    public static void main(String[] args) {
        String str_1 = "AaBbCcDd";
        String upperCase = "";
        String lowerCase = "";

        // использовать стек для хранения заглавных букв
        Stack<Character> upperStack = new Stack<>();
        //                                строчных букв
        Stack<Character> lowerStack = new Stack<>();

        for (int i = 0; i < str_1.length(); i++) {
            if (i % 2 == 0) { // заглавные на четных позициях
                upperStack.push(str_1.charAt(i));
            } else { // строчные на нечетных позициях
                lowerStack.push(str_1.charAt(i));
            }
        }

        // Извлекаем элементы из стека в обратном порядке
        while (!upperStack.isEmpty()) {
            upperCase = upperStack.pop() + upperCase; // добавляем в начало строки
        }

        while (!lowerStack.isEmpty()) {
            lowerCase = lowerStack.pop() + lowerCase; // добавляем в начало строки
        }


        System.out.println("Заглавные: " + upperCase);
        System.out.println("Строчные: " + lowerCase);
    }
}
