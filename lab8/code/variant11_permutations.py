# variant11_permutations.py
# Вариант 11 — Генерация всех перестановок строки (backtracking, учёт дубликатов)
#
# Комментарии:
# - Реализована безопасная генерация перестановок при наличии повторяющихся символов.
# - Используется backtracking + метка used[] для управления выбором символов.
# - Результат возвращается как список строк.
# - Временная сложность O(n * n!) и пространственная O(n) для стека и O(n * n!) для хранения результатов.

from typing import List

def permutations_of_string(s: str) -> List[str]:
    """
    Возвращает список всех уникальных перестановок строки s.
    Поддерживает повторяющиеся символы (не дублирует одинаковые перестановки).
    """
    if s == "":
        return [""]  # Единственная перестановка пустой строки — пустая строка

    # Преобразуем в отсортированный список символов — помогает легко избегать дублей
    chars = sorted(s)
    n = len(chars)
    used = [False] * n  # Массив для отслеживания использованных символов
    current: List[str] = []  # Текущая перестановка
    result: List[str] = []  # Список всех перестановок

    def backtrack():
        # Если собрали длину n — сохраняем результат
        if len(current) == n:
            result.append("".join(current))
            return
        prev_char = None  # Для пропуска одинаковых символов на одной глубине
        for i in range(n):
            if used[i]:
                continue
            # Пропуск: если текущий символ такой же, как предыдущий неподключённый, пропускаем,
            # чтобы избежать одинаковых перестановок (классический приём).
            if prev_char is not None and chars[i] == prev_char:
                continue
            used[i] = True
            current.append(chars[i])
            backtrack()
            # Откат
            current.pop()
            used[i] = False
            prev_char = chars[i]  # Запоминаем предыдущий символ

    backtrack()
    return result

if __name__ == "__main__":
    examples = [
        "abc",
        "aab",
        "",
        "abca"
    ]
    for s in examples:
        perms = permutations_of_string(s)
        print(f"string: {s!r} -> {len(perms)} permutations")
        # показываем первые несколько (чтобы не захламлять вывод)
        sample_count = min(20, len(perms))
        print("sample:", perms[:sample_count])
        print("---")
