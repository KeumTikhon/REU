import java.util.*;

public class TSP {
    public static void main(String[] args) {
        // Матрица смежности графа городов
        int[][] graph = {
            {0, 10, 15, 20},
            {10, 0, 35, 25},
            {15, 35, 0, 30},
            {20, 25, 30, 0}
        };
        int n = graph.length;
        List<Integer> cities = new ArrayList<>();
        
        // Создаем список городов (кроме стартового)
        for (int i = 1; i < n; i++) cities.add(i);
        
        int minPath = Integer.MAX_VALUE;
        
        // Перебор всех перестановок городов
        do {
            int currentPath = 0;
            int k = 0;  // Начинаем с города 0
            
            // Суммируем путь для текущей перестановки
            for (int i = 0; i < cities.size(); i++) {
                currentPath += graph[k][cities.get(i)];
                k = cities.get(i);
            }
            currentPath += graph[k][0];  // Возвращаемся в начальный город
            
            minPath = Math.min(minPath, currentPath);
            
        } while (nextPermutation(cities));
        
        System.out.println("Минимальная длина пути: " + minPath);
    }
    
    // Генерация следующей перестановки
    private static boolean nextPermutation(List<Integer> array) {
        // Алгоритм Нарайаны
        int i = array.size() - 2;
        while (i >= 0 && array.get(i) >= array.get(i + 1)) i--;
        if (i < 0) return false;
        
        int j = array.size() - 1;
        while (array.get(j) <= array.get(i)) j--;
        
        Collections.swap(array, i, j);
        Collections.reverse(array.subList(i + 1, array.size()));
        return true;
    }
}