import time
from main_old import LogProcessor as LogProcessor_old
from main import LogProcessor

def create_large_sample():
    with open('large_sample.log', 'w') as f:
        for i in range(1000):
            f.write(f"192.168.1.{i % 100} - ERROR: Test error {i}\n")
            f.write(f"192.168.2.{i % 50} - INFO: Test info {i}\n")
            f.write(f"192.168.3.{i % 30} - WARNING: Test warning {i}\n")

def run_test():
    print("Сравнение оптимизированного и неоптимизированного кода")
    
    # Создаем большой файл для теста
    create_large_sample()
    
    old_processor = LogProcessor_old()
    new_processor = LogProcessor()
    
    start = time.time()
    old_result = old_processor.process_logs('large_sample.log')
    old_time = time.time() - start
    
    start = time.time()
    new_result = new_processor.process_logs('large_sample.log')
    new_time = time.time() - start
    
    print(f"Неоптимизированная: {old_time:.2f} сек")
    print(f"Оптимизированная: {old_time:.2f} сек")
    print(f"Ускорение: {old_time/old_time:.1f} раз")
    
    # Проверяем, что результаты одинаковые
    assert old_result['stats']['total'] == new_result['stats']['total']
    assert old_result['unique_ips'] == new_result['unique_ips']
    print("Результаты новой и старой версий совпадают")

if __name__ == "__main__":
    run_test()