#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int main() {
    // Матрица смежности графа городов
    vector<vector<int>> graph = {
        {0, 10, 15, 20},
        {10, 0, 35, 25},
        {15, 35, 0, 30},
        {20, 25, 30, 0}
    };
    int n = graph.size();
    vector<int> cities;
    
    // Создаем список городов (кроме стартового)
    for (int i = 1; i < n; i++) cities.push_back(i);
    
    int min_path = INT_MAX;
    
    // Перебор всех перестановок городов
    do {
        int current_path = 0;
        int k = 0;  // Начинаем с города 0
        
        // Суммируем путь для текущей перестановки
        for (int i = 0; i < cities.size(); i++) {
            current_path += graph[k][cities[i]];
            k = cities[i];
        }
        current_path += graph[k][0];  // Возвращаемся в начальный город
        
        min_path = min(min_path, current_path);
        
    } while (next_permutation(cities.begin(), cities.end()));
    
    cout << "Минимальная длина пути: " << min_path << endl;
    return 0;
}