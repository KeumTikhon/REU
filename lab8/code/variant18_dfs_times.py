# variant18_dfs_times.py
# Вариант 18 — DFS графа с записью времени входа (time_in) и выхода (time_out)
#
# Комментарии:
# - Реализация стандартного рекурсивного DFS для неориентированного/ориентированного графа.
# - Глобальный счётчик времени увеличивается при заходе и при выходе из вершины.
# - Для ориентированных графов поведение учитывает направление ребер.
# - Программа выводит time_in, time_out и parent для каждой вершины.

from typing import List, Dict, Tuple

def dfs_with_times(adj: Dict[int, List[int]]) -> Tuple[Dict[int,int], Dict[int,int], Dict[int,int]]:
    """
    Выполняет DFS по графу, заданному списком смежности adj (словарь int -> list[int]).
    Возвращает три словаря: time_in, time_out, parent.
    """
    time_in: Dict[int, int] = {}  # Время входа в вершину
    time_out: Dict[int, int] = {}  # Время выхода из вершины
    parent: Dict[int, int] = {}  # Родитель каждой вершины в дереве DFS
    visited: Dict[int, bool] = {}  # Отслеживание посещённых вершин
    time = 0  # Глобальный счётчик времени

    # Инициализация
    for v in adj:
        visited[v] = False
        parent[v] = -1  # -1 означает, что у вершины нет родителя (корень компоненты)

    def dfs(v: int):
        nonlocal time
        visited[v] = True
        time += 1
        time_in[v] = time  # Фиксируем время входа в вершину

        # Для каждого соседа, если не посещён, рекурсивно посещаем
        for nei in adj[v]:
            if not visited.get(nei, False):
                parent[nei] = v  # Устанавливаем родителя для соседа
                dfs(nei)

        # После обхода всех соседей фиксируем время выхода
        time += 1
        time_out[v] = time

    # Запускаем DFS с каждой непосещённой вершины (чтобы покрыть несвязный граф)
    for v in sorted(adj.keys()):
        if not visited[v]:
            dfs(v)

    return time_in, time_out, parent

if __name__ == "__main__":
    # Пример ориентированного графа в виде словаря смежности
    graph_example = {
        1: [2, 3],
        2: [4],
        3: [4, 5],
        4: [6],
        5: [6],
        6: [],
        7: [8],   # компонент, не связанный с остальными — демонстрируем несвязный граф
        8: []
    }

    tin, tout, parent = dfs_with_times(graph_example)
    print("vertex | time_in | time_out | parent")
    for v in sorted(graph_example.keys()):
        print(f"{v:6} | {tin.get(v, '-') :7} | {tout.get(v, '-') :8} | {parent.get(v, -1)}")
