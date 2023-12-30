# Sample code using regular expressions for log parsing
import re

def analyze_logs(log_file):
    with open(log_file, 'r') as file:
        for line in file:
            if re.search('ERROR', line):
                # Send alert or take appropriate action
                print(f'Error found: {line}')

if __name__ == '__main__':
    log_file = sys.argv[1]
    analyze_logs(log_file)
