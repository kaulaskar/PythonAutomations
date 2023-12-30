# Log Analysis Script

def analyze_logs(log_file_path, keyword):
    try:
        with open(log_file_path, 'r') as log_file:
            for line in log_file:
                if keyword in line:
                    print(f"Found keyword '{keyword}' in log: {line}")
    except FileNotFoundError:
        print(f"Error: Log file not found at {log_file_path}")

if __name__ == "__main__":
    log_file_path = "/path/to/logfile.log"
    keyword_to_search = "ERROR"
    analyze_logs(log_file_path, keyword_to_search)
