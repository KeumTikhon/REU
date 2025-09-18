#include <iostream>
#include <vector>
#include <string>
#include <stack>

using namespace std;

int main() {
    vector<string> list_1 = {"a", "1", "b", "2", "c", "3"};
    vector<string> letters;
    vector<string> numbers;

    stack<string> letterStack;
    stack<string> numberStack;

    for (const string& item : list_1) {
        if (isdigit(item[0])) { // Проверяем, является ли первый символ цифрой
            numberStack.push(item);
        } else {
            letterStack.push(item);
        }
    }
    // Извлекаем элементы из стеков
    while (!letterStack.empty()) {
        letters.push_back(letterStack.top());
        letterStack.pop();
    }

    while (!numberStack.empty()) {
        numbers.push_back(numberStack.top());
        numberStack.pop();
    }

    // Выводим элементы на экран
    cout << "Буквы: ";
    for (int i = 0; i < letters.size(); i++) {
        cout << letters[i] << " ";
    }
    cout << endl;

    cout << "Числа: ";
    for (int i = 0; i < numbers.size(); i++) {
        cout << numbers[i] << " ";
    }
    cout << endl;


    return 0;
}
