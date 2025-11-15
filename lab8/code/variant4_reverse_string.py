# variant4_reverse_string.py
# Вариант 4 — Рекурсивный разворот строки
#
# Комментарии:
# - На каждом шаге функция берёт первый символ и рекурсивно разворачивает оставшуюся часть.
# - Возвращаем новую строку; не модифицируем исходный объект.
# - Для больших строк рекурсия может достигнуть лимита глубины (по умолчанию ~1000 в CPython).
#   При работе с длинными строками рекомендуется итеративный метод или sys.setrecursionlimit.

from typing import Tuple

def reverse_string(s: str) -> str:
    """
    Рекурсивно возвращает строку `s`, обращённую в обратном порядке.
    reverse("") -> ""
    reverse("a") -> "a"
    reverse("abc") -> reverse("bc") + "a"
    """
    # Базовый случай: пустая строка или один символ
    if len(s) <= 1:
        return s  # Если строка пустая или длиной 1, возвращаем её как есть
    # Рекурсивный случай: разворачиваем хвост, затем добавляем первый символ в конец
    return reverse_string(s[1:]) + s[0]

if __name__ == "__main__":
    samples: Tuple[str, ...] = (
        "",
        "a",
        "hello",
        "algorithm",
        "A man, a plan, a canal, Panama"
    )

    for s in samples:
        rev = reverse_string(s)
        print(f"orig: {repr(s)} -> reversed: {repr(rev)}")
