import psutil as pu

if __name__ == '__main__':
    # Lấy tỷ lệ sử dụng CPU
    cpu_usage = pu.cpu_percent(interval=1)
    print(f'CPU Usage: {cpu_usage}%')

    # Lấy thông tin sử dụng bộ nhớ
    memory_usage = pu.virtual_memory()
    print(f'Total Memory: {memory_usage.total / (1024 ** 3):.2f} GB')
    print(f'Used Memory: {memory_usage.used / (1024 ** 3):.2f} GB')
    print(f'Memory Usage: {memory_usage.percent}%')

    # In hàng tiêu đề
    print(f'{"PID":<10} {"Name":<30} {"CPU":<12} {"Memory":<10} {"User":<20}')
    
    # Duyệt và in thông tin các tiến trình
    for proc in pu.process_iter():
        try:
            # Chỉ in các tiến trình chiếm bộ nhớ > 100 MB
            if float(proc.memory_info().rss / (1024 ** 2)) > 100:
                pid = proc.pid
                name = proc.name() or 'N/A'
                cpu = f'{proc.cpu_percent(interval=0.1):.2f} %' or 'N/A'
                memory_usage = f'{proc.memory_info().rss / (1024 ** 2):.2f} MB' or 'N/A'
                user = proc.username() or 'N/A'

                print(f'{pid:<10} {name:<30} {cpu:<12} {memory_usage:<10} {user:<20}')
        except (pu.NoSuchProcess, pu.AccessDenied, pu.ZombieProcess):
            pass
