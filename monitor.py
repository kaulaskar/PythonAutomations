# Sample code using wsadmin scripting tool
def monitor_server_resources(server_name):
    server = AdminControl.queryNames('type=Server,process=' + server_name + ',*')
    cpu_usage = AdminControl.getAttribute(server, 'percentCpuUsage')
    memory_usage = AdminControl.getAttribute(server, 'usedMemory')

    print(f'{server_name} - CPU Usage: {cpu_usage}%, Memory Usage: {memory_usage} bytes')

if __name__ == '__main__':
    server_name = sys.argv[1]
    monitor_server_resources(server_name)

