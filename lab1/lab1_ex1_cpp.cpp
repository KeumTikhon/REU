#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main() {
    string str_1 = "AaBbCcDd";
    string upper_case = "";
    string lower_case = "";

    // использовать стек для хранения заглавных букв
    stack<char> upper_stack;
    //                                строчных букв
    stack<char> lower_stack;

    for (int i = 0; i < str_1.length(); ++i) {
        if (i % 2 == 0) { // заглавные на четных позициях
            upper_stack.push(str_1[i]);
        } else { // строчные на нечетных позициях
            lower_stack.push(str_1[i]);
        }
    }

    // Переложить символы из стека в строку (в обратном порядке)
    while (!upper_stack.empty()) {
        upper_case = upper_stack.top() + upper_case; // Добавляем в начало
        upper_stack.pop();
    }

    while (!lower_stack.empty()) {
        lower_case = lower_stack.top() + lower_case; // Добавляем в начало
        lower_stack.pop();
    }


    cout << "Заглавные: " << upper_case << endl;
    cout << "Строчные: " << lower_case << endl;

    return 0;
}
