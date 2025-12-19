from typing import List, Tuple

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"({self.x}, {self.y})"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def cross_product(o: Point, a: Point, b: Point) -> float:
    """
    Векторное произведение для определения ориентации трёх точек
    Возвращает:
        > 0: левый поворот (против часовой)
        = 0: коллинеарные точки
        < 0: правый поворот (по часовой)
    """
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)


def polar_angle(anchor: Point, p: Point) -> float:
    """Вычислить полярный угол точки p относительно опорной точки anchor"""
    import math
    return math.atan2(p.y - anchor.y, p.x - anchor.x)


def distance_squared(p1: Point, p2: Point) -> float:
    """Вычислить квадрат расстояния между двумя точками (для сравнения)"""
    return (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2


def graham_scan(points: List[Point]) -> List[Point]:
    """
    Алгоритм Graham Scan для поиска выпуклой оболочки
    
    Args:
        points: список точек на плоскости
    
    Returns:
        список точек, образующих выпуклую оболочку (против часовой стрелки)
    """
    
    n = len(points)
    if n < 3:
        return sorted(points, key=lambda p: (p.x, p.y))
    
    # Шаг 1: Найти опорную точку (с минимальной Y, потом с минимальной X)
    anchor = min(points, key=lambda p: (p.y, p.x))
    
    # Шаг 2: Отсортировать остальные точки по полярному углу
    other_points = [p for p in points if p != anchor]
    
    # Сортируем по углу, если углы равны - по расстоянию
    sorted_points = sorted(
        other_points,
        key=lambda p: (polar_angle(anchor, p), distance_squared(anchor, p))
    )
    
    # Шаг 3: Graham Scan - построение выпуклой оболочки
    hull = [anchor]
    
    for point in sorted_points:
        # Пока в оболочке менее 2 точек или последний поворот - левый
        while len(hull) > 1 and cross_product(hull[-2], hull[-1], point) <= 0:
            hull.pop()
        hull.append(point)
    
    return hull


def print_convex_hull(points: List[Point]) -> None:
    """Вычислить и вывести выпуклую оболочку"""
    hull = graham_scan(points)
    print(f"Выпуклая оболочка ({len(hull)} вершин):")
    for i, point in enumerate(hull):
        print(f"  {i+1}. {point}")
    return hull


# Пример использования
if __name__ == "__main__":
    # Пример 1: простой случай
    print("Пример 1: 8 точек")
    points1 = [
        Point(0, 3),
        Point(1, 1),
        Point(2, 2),
        Point(4, 4),
        Point(0, 0),
        Point(1, 2),
        Point(3, 1),
        Point(3, 3)
    ]
    
    print("Входные точки:")
    for i, p in enumerate(points1):
        print(f"  {i+1}. {p}")
    
    hull1 = print_convex_hull(points1)
    
    # Пример 2: случайные точки
    print("\n" + "="*50)
    print("Пример 2: 15 случайных точек")
    import random
    random.seed(42)
    points2 = [Point(random.randint(0, 20), random.randint(0, 20)) for _ in range(15)]
    
    print("Входные точки:")
    for i, p in enumerate(points2):
        print(f"  {i+1}. {p}")
    
    hull2 = print_convex_hull(points2)
    
    # Пример 3: вырожденный случай (коллинеарные точки)
    print("\n" + "="*50)
    print("Пример 3: коллинеарные точки на прямой")
    points3 = [
        Point(0, 0),
        Point(1, 1),
        Point(2, 2),
        Point(3, 3),
        Point(1.5, 1.5)
    ]
    
    print("Входные точки:")
    for i, p in enumerate(points3):
        print(f"  {i+1}. {p}")
    
    hull3 = print_convex_hull(points3)
