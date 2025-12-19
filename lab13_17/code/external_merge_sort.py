import heapq
import os
from typing import List

class ExternalMergeSort:
    def __init__(self, memory_size=1000):
        """
        memory_size: количество элементов, которые можно держать в памяти одновременно
        """
        self.memory_size = memory_size
        self.temp_files = []
        self.temp_file_counter = 0
    
    def sort_file(self, input_file, output_file):
        """Сортировка большого файла через external merge sort"""
        
        # Фаза 1: разбиение и сортировка
        print(f"Фаза 1: Разбиение файла на отсортированные блоки...")
        self.phase_1_split_and_sort(input_file)
        
        # Фаза 2: слияние отсортированных блоков
        print(f"Фаза 2: Слияние блоков...")
        self.phase_2_merge(output_file)
        
        print(f"Сортировка завершена! Результат: {output_file}")
    
    def phase_1_split_and_sort(self, input_file):
        """
        Разбиваем входной файл на блоки, каждый блок сортируем в памяти
        и записываем во временный файл
        """
        self.temp_files = []
        
        with open(input_file, 'r') as f:
            block = []
            
            for line in f:
                value = int(line.strip())
                block.append(value)
                
                # Когда блок заполнен до размера памяти
                if len(block) >= self.memory_size:
                    self._write_sorted_block(block)
                    block = []
            
            # Последний оставшийся блок
            if block:
                self._write_sorted_block(block)
    
    def _write_sorted_block(self, block):
        """Отсортировать блок и записать во временный файл"""
        block.sort()
        
        temp_filename = f"temp_{self.temp_file_counter}.txt"
        self.temp_file_counter += 1
        self.temp_files.append(temp_filename)
        
        with open(temp_filename, 'w') as f:
            for value in block:
                f.write(f"{value}\n")
        
        print(f"  Написан блок {len(self.temp_files)}: {temp_filename} ({len(block)} элементов)")
    
    def phase_2_merge(self, output_file):
        """
        Слияние всех отсортированных временных файлов в один выходной файл
        Используем min-heap для эффективного выбора минимального элемента
        """
        
        # Открываем все временные файлы
        file_handles = []
        heap = []  # Min-heap элементов (value, file_index, line_index)
        
        for i, temp_file in enumerate(self.temp_files):
            fh = open(temp_file, 'r')
            file_handles.append(fh)
            
            # Читаем первый элемент из каждого файла
            line = fh.readline()
            if line:
                value = int(line.strip())
                heapq.heappush(heap, (value, i))
        
        # Слияние: вытаскиваем минимум, записываем, читаем следующий
        with open(output_file, 'w') as out:
            while heap:
                # Извлекаем минимальный элемент
                min_value, file_idx = heapq.heappop(heap)
                out.write(f"{min_value}\n")
                
                # Читаем следующий элемент из того же файла
                line = file_handles[file_idx].readline()
                if line:
                    value = int(line.strip())
                    heapq.heappush(heap, (value, file_idx))
        
        # Закрываем все файловые дескрипторы
        for fh in file_handles:
            fh.close()
        
        # Удаляем временные файлы
        for temp_file in self.temp_files:
            if os.path.exists(temp_file):
                os.remove(temp_file)
                print(f"  Удалён временный файл: {temp_file}")


# Пример использования
if __name__ == "__main__":
    import random
    
    # Создаём большой входной файл для примера
    input_file = "large_input.txt"
    output_file = "sorted_output.txt"
    
    print("Создание входного файла...")
    with open(input_file, 'w') as f:
        for _ in range(10000):
            f.write(f"{random.randint(1, 100000)}\n")
    
    # Сортируем с размером памяти = 1000 элементов
    sorter = ExternalMergeSort(memory_size=1000)
    sorter.sort_file(input_file, output_file)
    
    # Проверяем результат
    print("\nПроверка первых 20 строк выходного файла:")
    with open(output_file, 'r') as f:
        for i, line in enumerate(f):
            if i >= 20:
                break
            print(f"  {line.strip()}", end="  ")
            if (i + 1) % 5 == 0:
                print()
