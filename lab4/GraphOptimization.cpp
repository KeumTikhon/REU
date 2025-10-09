#include <iostream>
#include <vector>
#include <queue>
#include <climits>
#include <utility>
#include <string>

using namespace std;

// Структура для представления ребра в графе
struct Edge {
    int target;    // Целевая вершина
    int weight;    // Вес ребра
    
    Edge(int t, int w) : target(t), weight(w) {}
};

// Реализация алгоритма Дейкстры для поиска кратчайших путей
vector<int> dijkstra(const vector<vector<Edge>>& graph, int start) {
    int n = graph.size();
    vector<int> distances(n, INT_MAX);    // Вектор кратчайших расстояний
    vector<bool> visited(n, false);       // Вектор посещенных вершин
    
    // Инициализация: расстояние до стартовой вершины = 0
    distances[start] = 0;
    
    // Приоритетная очередь для хранения пар (расстояние, вершина)
    // greater<> обеспечивает минимальную кучу (min-heap)
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, start});
    
    while (!pq.empty()) {
        int currentDist = pq.top().first;
        int currentNode = pq.top().second;
        pq.pop();
        
        // Пропускаем если вершина уже обработана
        if (visited[currentNode]) continue;
        visited[currentNode] = true;
        
        // Обновляем расстояния до всех соседних вершин
        for (const Edge& edge : graph[currentNode]) {
            int newDist = currentDist + edge.weight;
            // Если найден более короткий путь - обновляем
            if (newDist < distances[edge.target]) {
                distances[edge.target] = newDist;
                pq.push({newDist, edge.target});
            }
        }
    }
    
    return distances;
}

// ЗАДАНИЕ 1: Оптимизация транспортной сети
void optimizeTransportNetwork() {
    cout << "=== ЗАДАНИЕ 1: ОПТИМИЗАЦИЯ ТРАНСПОРТНОЙ СЕТИ ===" << endl;
    cout << "Цель: найти кратчайшие пути между складами для минимизации логистических затрат" << endl;
    
    // Создаем граф транспортной сети (5 складов)
    vector<vector<Edge>> transportGraph(5);
    
    // Добавляем ребра с расстояниями между складами
    transportGraph[0].push_back(Edge(1, 50));  // Склад 0 -> Склад 1: 50 км
    transportGraph[0].push_back(Edge(2, 30));  // Склад 0 -> Склад 2: 30 км
    transportGraph[1].push_back(Edge(3, 40));  // Склад 1 -> Склад 3: 40 км
    transportGraph[2].push_back(Edge(3, 20));  // Склад 2 -> Склад 3: 20 км
    transportGraph[2].push_back(Edge(4, 35));  // Склад 2 -> Склад 4: 35 км
    transportGraph[3].push_back(Edge(4, 25));  // Склад 3 -> Склад 4: 25 км
    
    // Вычисляем кратчайшие пути от главного склада
    vector<int> transportDistances = dijkstra(transportGraph, 0);
    
    // Выводим результаты
    cout << "\nКратчайшие расстояния от главного склада:" << endl;
    vector<string> warehouseNames = {"Главный склад", "Склад Северный", "Склад Восточный", 
                                    "Склад Южный", "Склад Западный"};
    for (int i = 0; i < transportDistances.size(); i++) {
        cout << warehouseNames[i] << " (" << i << "): " << transportDistances[i] << " км" << endl;
    }
    
    // Анализ результатов
    cout << "\nАнализ оптимальных маршрутов:" << endl;
    cout << "Лучший маршрут до Южного склада: Главный → Восточный → Южный" << endl;
    cout << "Расстояние: " << transportDistances[3] << " км" << endl;
}

// ЗАДАНИЕ 2: Оптимизация сетевой топологии
void optimizeNetworkTopology() {
    cout << "\n=== ЗАДАНИЕ 2: ОПТИМИЗАЦИЯ СЕТЕВОЙ ТОПОЛОГИИ ===" << endl;
    cout << "Цель: найти пути с минимальной задержкой между серверами" << endl;
    
    // Создаем граф сетевой топологии (6 серверов)
    vector<vector<Edge>> networkGraph(6);
    
    // Добавляем ребра с задержками передачи
    networkGraph[0].push_back(Edge(1, 10));  // Сервер 0 -> Сервер 1: 10 мс
    networkGraph[0].push_back(Edge(2, 15));  // Сервер 0 -> Сервер 2: 15 мс
    networkGraph[1].push_back(Edge(3, 12));  // Сервер 1 -> Сервер 3: 12 мс
    networkGraph[1].push_back(Edge(4, 8));   // Сервер 1 -> Сервер 4: 8 мс
    networkGraph[2].push_back(Edge(4, 20));  // Сервер 2 -> Сервер 4: 20 мс
    networkGraph[3].push_back(Edge(5, 5));   // Сервер 3 -> Сервер 5: 5 мс
    networkGraph[4].push_back(Edge(5, 6));   // Сервер 4 -> Сервер 5: 6 мс
    
    // Вычисляем минимальные задержки
    vector<int> networkDistances = dijkstra(networkGraph, 0);
    
    // Выводим результаты
    cout << "\nМинимальные задержки от главного сервера:" << endl;
    vector<string> serverNames = {"Главный сервер", "Сервер БД", "Сервер приложений", 
                                 "Файловый сервер", "Веб-сервер", "Резервный сервер"};
    for (int i = 0; i < networkDistances.size(); i++) {
        cout << serverNames[i] << " (" << i << "): " << networkDistances[i] << " мс" << endl;
    }
    
    // Анализ оптимальных маршрутов
    cout << "\nАнализ оптимальных маршрутов:" << endl;
    cout << "Оптимальный маршрут до резервного сервера: Главный → Сервер БД → Веб-сервер → Резервный" << endl;
    cout << "Суммарная задержка: " << networkDistances[5] << " мс" << endl;
}

int main() {
    // Выполняем оба задания
    optimizeTransportNetwork();
    optimizeNetworkTopology();
    
    cout << "\n=== РЕЗЮМЕ ===" << endl;
    cout << "Оба примера демонстрируют практическое применение алгоритма Дейкстры" << endl;
    cout << "для решения реальных задач оптимизации в различных областях" << endl;
    
    return 0;
}