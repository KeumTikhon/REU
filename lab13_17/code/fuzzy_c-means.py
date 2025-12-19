import numpy as np
from typing import Tuple

class FuzzyCMeans:
    def __init__(self, n_clusters: int = 3, m: float = 2.0, 
                 max_iter: int = 100, epsilon: float = 1e-5):
        """
        Fuzzy C-Means кластеризация
        
        Args:
            n_clusters: количество кластеров (c)
            m: параметр фаззификации (обычно 2, m > 1)
            max_iter: максимальное количество итераций
            epsilon: порог сходимости
        """
        self.n_clusters = n_clusters
        self.m = m
        self.max_iter = max_iter
        self.epsilon = epsilon
        
        self.U = None  # Матрица принадлежности (c × n)
        self.centers = None  # Центроиды кластеров (c × d)
        self.iteration_count = 0
    
    def fit(self, X: np.ndarray) -> 'FuzzyCMeans':
        """
        Обучение модели на данных X
        
        Args:
            X: матрица данных (n × d), где n - количество точек, d - размерность
        """
        n_samples, n_features = X.shape
        
        # Инициализация матрицы принадлежности U случайными значениями
        self.U = np.random.dirichlet(np.ones(self.n_clusters), size=n_samples).T
        
        # Основной итерационный цикл
        for iteration in range(self.max_iter):
            U_old = self.U.copy()
            
            # Шаг 1: Обновление центроидов
            self.centers = self._update_centers(X)
            
            # Шаг 2: Обновление матрицы принадлежности U
            self.U = self._update_membership(X)
            
            # Шаг 3: Проверка сходимости
            diff = np.linalg.norm(self.U - U_old)
            self.iteration_count = iteration + 1
            
            if iteration % 10 == 0:
                cost = self._calculate_cost(X)
                print(f"  Итерация {iteration + 1}: сходимость = {diff:.6f}, стоимость = {cost:.6f}")
            
            if diff < self.epsilon:
                print(f"Сходимость достигнута на итерации {iteration + 1}")
                break
        
        return self
    
    def _update_centers(self, X: np.ndarray) -> np.ndarray:
        """
        Обновление центроидов кластеров
        V[i] = (∑ U[i,j]^m · X[j]) / (∑ U[i,j]^m)
        """
        Um = self.U ** self.m
        centers = np.zeros((self.n_clusters, X.shape[1]))
        
        for i in range(self.n_clusters):
            numerator = np.dot(Um[i], X)  # ∑ U[i,j]^m · X[j]
            denominator = np.sum(Um[i])   # ∑ U[i,j]^m
            centers[i] = numerator / denominator
        
        return centers
    
    def _update_membership(self, X: np.ndarray) -> np.ndarray:
        """
        Обновление матрицы принадлежности U
        U[i,j] = 1 / (∑_k (d[i,j] / d[k,j])^(2/(m-1)))
        """
        n_samples = X.shape[0]
        distances = np.zeros((self.n_clusters, n_samples))
        
        # Вычисляем евклидовы расстояния от каждой точки до каждого центроида
        for i in range(self.n_clusters):
            distances[i] = np.linalg.norm(X - self.centers[i], axis=1)
        
        # Избегаем деления на ноль
        distances = np.fmax(distances, 1e-10)
        
        # Вычисляем показатель степени
        power = 2.0 / (self.m - 1)
        
        # U[i,j] = 1 / (∑_k (d[i,j] / d[k,j])^power)
        U = np.zeros((self.n_clusters, n_samples))
        for i in range(self.n_clusters):
            for j in range(n_samples):
                denominator = np.sum((distances[i, j] / distances[:, j]) ** power)
                U[i, j] = 1.0 / denominator
        
        return U
    
    def _calculate_cost(self, X: np.ndarray) -> float:
        """Вычислить функцию стоимости (целевую функцию)"""
        cost = 0.0
        Um = self.U ** self.m
        
        for i in range(self.n_clusters):
            for j in range(X.shape[0]):
                distance = np.linalg.norm(X[j] - self.centers[i])
                cost += Um[i, j] * (distance ** 2)
        
        return cost
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Предсказать кластеры для новых данных (жёсткое назначение)
        Возвращает индекс кластера с наибольшей степенью принадлежности
        """
        n_samples = X.shape[0]
        labels = np.zeros(n_samples, dtype=int)
        
        for j in range(n_samples):
            # Вычисляем расстояния
            distances = np.array([
                np.linalg.norm(X[j] - self.centers[i])
                for i in range(self.n_clusters)
            ])
            # Кластер с минимальным расстоянием
            labels[j] = np.argmin(distances)
        
        return labels
    
    def get_membership_degrees(self) -> np.ndarray:
        """Получить полную матрицу степеней принадлежности U"""
        return self.U
    
    def get_centers(self) -> np.ndarray:
        """Получить центроиды кластеров"""
        return self.centers


# Пример использования
if __name__ == "__main__":
    # Создаём синтетические данные
    print("Создание синтетических данных...")
    np.random.seed(42)
    
    # Три кластера
    cluster1 = np.random.randn(50, 2) + np.array([0, 0])
    cluster2 = np.random.randn(50, 2) + np.array([5, 5])
    cluster3 = np.random.randn(50, 2) + np.array([5, 0])
    
    X = np.vstack([cluster1, cluster2, cluster3])
    
    print(f"Данные: {X.shape[0]} точек, {X.shape[1]} размерность\n")
    
    # Применяем Fuzzy C-Means
    print("Запуск Fuzzy C-Means с 3 кластерами...")
    fcm = FuzzyCMeans(n_clusters=3, m=2.0, max_iter=100, epsilon=1e-5)
    fcm.fit(X)
    
    print(f"\nЦентроиды кластеров:")
    for i, center in enumerate(fcm.get_centers()):
        print(f"  Кластер {i}: ({center[0]:.2f}, {center[1]:.2f})")
    
    # Жёсткое назначение кластеров
    labels = fcm.predict(X)
    print(f"\nКоличество точек в каждом кластере:")
    for i in range(fcm.n_clusters):
        count = np.sum(labels == i)
        print(f"  Кластер {i}: {count} точек")
    
    # Степени принадлежности для первых 5 точек
    U = fcm.get_membership_degrees()
    print(f"\nСтепени принадлежности первых 5 точек:")
    print("     Кластер 0  Кластер 1  Кластер 2")
    for j in range(min(5, X.shape[0])):
        print(f"Точка {j}: {U[0, j]:.4f}      {U[1, j]:.4f}      {U[2, j]:.4f}")
