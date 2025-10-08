import re

class LogProcessor:
    def __init__(self):
        self.ip_pattern = re.compile(r'\d+\.\d+\.\d+\.\d+')
    
    def process_logs(self, filename):
        """Обработка логов"""
        stats = {'total': 0, 'errors': 0, 'warnings': 0, 'info': 0}
        ips = set()
        errors = []
        
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                for line in file:
                    stats['total'] += 1
                    line_lower = line.lower()
                    
                    # Анализ типа сообщения
                    if 'error' in line_lower:
                        stats['errors'] += 1
                        errors.append(line.strip())
                    elif 'warning' in line_lower:
                        stats['warnings'] += 1
                    elif 'info' in line_lower:
                        stats['info'] += 1
                    
                    # Поиск IP-адресов
                    ip_match = self.ip_pattern.search(line)
                    if ip_match:
                        ips.add(ip_match.group())
            
            return {
                'stats': stats,
                'unique_ips': len(ips),
                'sample_errors': errors[:3]
            }
            
        except FileNotFoundError:
            print(f"File {filename} not found")
            return None

def main():

    processor = LogProcessor()

    print("LOG PROCESSOR")
    filename = input("Enter file name (default: sample.log): ").strip()
    
    if not filename:
        filename = "sample.log"

    result = processor.process_logs("logs/"+filename)
    
    if result:
        print("\nResults:")
        print(f"Total: {result['stats']['total']}")
        print(f"Errors: {result['stats']['errors']}")
        print(f"Warnings: {result['stats']['warnings']}") 
        print(f"Info messages: {result['stats']['info']}")
        print(f"Unique IP addresses: {result['unique_ips']}")

        if result['sample_errors']:
            print("\nError examples:")
            for error in result['sample_errors']:
                print(f"  - {error}")
        

if __name__ == "__main__":
    main()