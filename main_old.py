import re

class LogProcessor:
    def __init__(self):
        pass
    
    def process_logs(self, filename):
        """Обработка логов с вложенными циклами"""
        logs = []
        
        with open(filename, 'r', encoding='utf-8') as file:
            logs = file.readlines()
        
        ip_addresses = []
        results = {}
        
        # сбор IP
        for log in logs:
            ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', log)
            if ip_match:
                ip = ip_match.group()
                if ip not in ip_addresses:
                    ip_addresses.append(ip)
        
        # обработка
        stats = {'total': 0, 'errors': 0, 'warnings': 0, 'info': 0}
        for ip in ip_addresses:
            for log in logs:
                if ip in log:
                    stats['total'] += 1
                    if 'ERROR' in log:
                        stats['errors'] += 1
                    elif 'WARNING' in log:
                        stats['warnings'] += 1
                    elif 'INFO' in log:
                        stats['info'] += 1

        
        return {
            'stats': stats,
            'unique_ips': len(ip_addresses)
        }

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
        

if __name__ == "__main__":
    main()