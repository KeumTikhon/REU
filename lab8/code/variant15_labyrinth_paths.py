# variant15_labyrinth_paths.py
# Вариант 15 — Генерация всех путей в лабиринте 5x5 (backtracking)
#
# Комментарии:
# - Мы ищем все простые пути (без повторного посещения клеток) от стартовой клетки до целевой.
# - Поддерживаем движение 4-направления: право, вниз, влево, вверх (можно поменять порядок).
# - Чтобы вывод не взрывался, примерный лабиринт содержит преграды; для полного пустого поля число путей
#   может быть огромно (фактически комбинаторный взрыв).
#
# Формат лабиринта:
# 0 — свободная клетка
# 1 — стена / непреодолимая клетка

from typing import List, Tuple

# Размер лабиринта фиксировать в 5x5 согласно условию
N = 5

# Возможные движения: (dx, dy) с метками для читаемости
MOVES: List[Tuple[int,int,str]] = [
    (0, 1, "R"),  # вправо
    (1, 0, "D"),  # вниз
    (0, -1, "L"), # влево
    (-1, 0, "U")  # вверх
]

def find_all_paths(maze: List[List[int]],
                   start: Tuple[int,int],
                   end: Tuple[int,int],
                   max_paths: int = 10000) -> List[List[Tuple[int,int]]]:
    """
    Находит все пути от start до end в maze (матрица N x N), не посещая клетки повторно.
    Возвращает список путей, где путь — список координат (x,y).
    max_paths ограничивает число собираемых путей (защита от взрывного роста).
    """
    n = len(maze)
    if n != N or any(len(row) != N for row in maze):
        raise ValueError(f"maze must be {N}x{N}")

    sx, sy = start
    ex, ey = end

    # Быстрая проверка: если старт или цель — стена, нет путей
    if maze[sx][sy] == 1 or maze[ex][ey] == 1:
        return []

    visited = [[False]*n for _ in range(n)]  # Матрица посещённых клеток
    paths: List[List[Tuple[int,int]]] = []  # Список всех найденных путей
    current: List[Tuple[int,int]] = []  # Текущий путь

    def backtrack(x: int, y: int):
        # Ограничение: не собирать слишком много путей
        if len(paths) >= max_paths:
            return
        # Если выходим за границы или попадаем в стену или уже посещённую клетку — откат
        if not (0 <= x < n and 0 <= y < n) or maze[x][y] == 1 or visited[x][y]:
            return

        # Добавляем текущую клетку в путь и помечаем как посещённую
        visited[x][y] = True
        current.append((x, y))

        # Если достигли цели — сохраняем копию текущего пути
        if (x, y) == (ex, ey):
            paths.append(current.copy())
        else:
            # Иначе пробуем все направления (порядок определяет порядок путей)
            for dx, dy, _label in MOVES:
                nx, ny = x + dx, y + dy
                backtrack(nx, ny)

        # Откат: снимаем отметку посещённости и удаляем клетку из текущего пути
        current.pop()
        visited[x][y] = False

    backtrack(sx, sy)
    return paths

if __name__ == "__main__":
    # Пример лабиринта 5x5 (0 — свободно, 1 — стена)
    # Дизайн лабиринта намеренно даёт небольшое, но не тривиальное число путей.
    maze_example = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
    ]
    start = (0, 0)  # верхний левый угол
    end = (4, 4)    # нижний правый угол

    paths = find_all_paths(maze_example, start, end, max_paths=1000)
    print(f"Found {len(paths)} path(s) from {start} to {end} (showing up to 10):\n")
    for i, p in enumerate(paths[:10], 1):
        # Для удобства печатаем последовательность позиций и краткую строку направлений
        coords = "->".join(f"({x},{y})" for x,y in p)
        directions = []
        for (x1,y1), (x2,y2) in zip(p, p[1:]):
            if x2 == x1 and y2 == y1+1:
                directions.append("R")
            elif x2 == x1+1 and y2 == y1:
                directions.append("D")
            elif x2 == x1 and y2 == y1-1:
                directions.append("L")
            elif x2 == x1-1 and y2 == y1:
                directions.append("U")
            else:
                directions.append("?")
        print(f"Path {i}: length={len(p)}; dirs={''.join(directions)}")
        print(f"  coords: {coords}\n")
