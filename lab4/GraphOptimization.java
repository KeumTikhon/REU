import java.util.*;

public class GraphOptimization {
    
    // Класс для представления ребра в графе
    static class Edge {
        int target;    // Целевая вершина
        int weight;    // Вес ребра (расстояние, задержка и т.д.)
        
        Edge(int target, int weight) {
            this.target = target;
            this.weight = weight;
        }
    }
    
    // Реализация алгоритма Дейкстры для поиска кратчайших путей
    public static int[] dijkstra(List<List<Edge>> graph, int start) {
        int n = graph.size();
        int[] distances = new int[n];      // Массив для хранения кратчайших расстояний
        boolean[] visited = new boolean[n]; // Массив для отслеживания посещенных вершин
        
        // Инициализация: все расстояния бесконечны, кроме стартовой вершины
        Arrays.fill(distances, Integer.MAX_VALUE);
        distances[start] = 0;
        
        // Приоритетная очередь для эффективного выбора вершины с минимальным расстоянием
        // Хранит пары [вершина, расстояние]
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
        pq.offer(new int[]{start, 0});
        
        while (!pq.isEmpty()) {
            int[] current = pq.poll();
            int node = current[0];
            int dist = current[1];
            
            // Пропускаем если уже обработали эту вершину
            if (visited[node]) continue;
            visited[node] = true;
            
            // Обновляем расстояния до всех соседей текущей вершины
            for (Edge edge : graph.get(node)) {
                int newDist = dist + edge.weight;
                // Если найден более короткий путь - обновляем расстояние
                if (newDist < distances[edge.target]) {
                    distances[edge.target] = newDist;
                    pq.offer(new int[]{edge.target, newDist});
                }
            }
        }
        
        return distances;
    }
    
    // ЗАДАНИЕ 1: Оптимизация транспортной сети между складами
    public static void optimizeTransportNetwork() {
        System.out.println("=== ЗАДАНИЕ 1: ОПТИМИЗАЦИЯ ТРАНСПОРТНОЙ СЕТИ ===");
        System.out.println("Цель: найти кратчайшие пути между складами для минимизации логистических затрат");
        
        // Создаем граф транспортной сети (5 складов)
        List<List<Edge>> transportGraph = new ArrayList<>();
        for (int i = 0; i < 5; i++) {
            transportGraph.add(new ArrayList<>());
        }
        
        // Определяем расстояния между складами (в километрах)
        // Склад 0 - главный распределительный центр
        transportGraph.get(0).add(new Edge(1, 50));  // Склад 0 -> Склад 1: 50 км
        transportGraph.get(0).add(new Edge(2, 30));  // Склад 0 -> Склад 2: 30 км
        transportGraph.get(1).add(new Edge(3, 40));  // Склад 1 -> Склад 3: 40 км
        transportGraph.get(2).add(new Edge(3, 20));  // Склад 2 -> Склад 3: 20 км
        transportGraph.get(2).add(new Edge(4, 35));  // Склад 2 -> Склад 4: 35 км
        transportGraph.get(3).add(new Edge(4, 25));  // Склад 3 -> Склад 4: 25 км
        
        // Находим кратчайшие пути от главного склада (0) до всех остальных
        int[] transportDistances = dijkstra(transportGraph, 0);
        
        // Выводим результаты
        System.out.println("\nКратчайшие расстояния от главного склада:");
        String[] warehouseNames = {"Главный склад", "Склад Северный", "Склад Восточный", 
                                  "Склад Южный", "Склад Западный"};
        for (int i = 0; i < transportDistances.length; i++) {
            System.out.println(warehouseNames[i] + " (" + i + "): " + 
                             transportDistances[i] + " км");
        }
        
        // Анализ оптимальных маршрутов
        System.out.println("\nАнализ оптимальных маршрутов:");
        System.out.println("Лучший маршрут до Южного склада: Главный → Восточный → Южный");
        System.out.println("Расстояние: " + transportDistances[3] + " км");
    }
    
    // ЗАДАНИЕ 2: Оптимизация сетевой топологии
    public static void optimizeNetworkTopology() {
        System.out.println("\n=== ЗАДАНИЕ 2: ОПТИМИЗАЦИЯ СЕТЕВОЙ ТОПОЛОГИИ ===");
        System.out.println("Цель: найти пути с минимальной задержкой между серверами");
        
        // Создаем граф сетевой топологии (6 серверов)
        List<List<Edge>> networkGraph = new ArrayList<>();
        for (int i = 0; i < 6; i++) {
            networkGraph.add(new ArrayList<>());
        }
        
        // Определяем задержки передачи между серверами (в миллисекундах)
        // Сервер 0 - главный узел сети
        networkGraph.get(0).add(new Edge(1, 10));  // Сервер 0 -> Сервер 1: 10 мс
        networkGraph.get(0).add(new Edge(2, 15));  // Сервер 0 -> Сервер 2: 15 мс
        networkGraph.get(1).add(new Edge(3, 12));  // Сервер 1 -> Сервер 3: 12 мс
        networkGraph.get(1).add(new Edge(4, 8));   // Сервер 1 -> Сервер 4: 8 мс
        networkGraph.get(2).add(new Edge(4, 20));  // Сервер 2 -> Сервер 4: 20 мс
        networkGraph.get(3).add(new Edge(5, 5));   // Сервер 3 -> Сервер 5: 5 мс
        networkGraph.get(4).add(new Edge(5, 6));   // Сервер 4 -> Сервер 5: 6 мс
        
        // Находим минимальные задержки от главного сервера до всех остальных
        int[] networkDistances = dijkstra(networkGraph, 0);
        
        // Выводим результаты
        System.out.println("\nМинимальные задержки от главного сервера:");
        String[] serverNames = {"Главный сервер", "Сервер БД", "Сервер приложений", 
                               "Файловый сервер", "Веб-сервер", "Резервный сервер"};
        for (int i = 0; i < networkDistances.length; i++) {
            System.out.println(serverNames[i] + " (" + i + "): " + 
                             networkDistances[i] + " мс");
        }
        
        // Анализ оптимальных маршрутов
        System.out.println("\nАнализ оптимальных маршрутов:");
        System.out.println("Оптимальный маршрут до резервного сервера: Главный → Сервер БД → Веб-сервер → Резервный");
        System.out.println("Суммарная задержка: " + networkDistances[5] + " мс");
    }
    
    public static void main(String[] args) {
        // Выполняем оба задания последовательно
        optimizeTransportNetwork();
        optimizeNetworkTopology();
        
        System.out.println("\n=== РЕЗЮМЕ ===");
        System.out.println("Оба примера демонстрируют практическое применение алгоритма Дейкстры");
        System.out.println("для решения реальных задач оптимизации в различных областях");
    }
}