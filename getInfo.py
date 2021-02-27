import platform
import psutil


#Send data to flas server using requests module
def convert_bytes(bytes):
    factor = 1024
    listValues = ['B', 'KB', 'MB', 'GB', "TB", 'PB']
    for unit in listValues:
        if bytes < factor:
            return (str(bytes) + ' ' + unit)
        bytes = bytes/factor


#System Information

system = platform.uname()

operating_system = system.system
node = system.node
release = system.release
version = system.version
machine = system.machine
processor = system.processor

#CPU Information

phys_cores = psutil.cpu_count(logical=False)
Total_cores = psutil.cpu_count(logical=True)

frequency = psutil.cpu_freq()
min_freq = frequency.min
max_freq = frequency.max
curr_freq = frequency.current

total_cpu_usage = psutil.cpu_percent()

#memory usage

memory = psutil.virtual_memory()

total_mem = convert_bytes(memory.total)
available_mem = convert_bytes(memory.available)
used_mem = convert_bytes(memory.used)
percentage_mem = (str(memory.percent) + '%')


#disk Information

parts = psutil.disk_partitions()

dict_parts = {}

for partition in parts:
    partition_usage = psutil.disk_usage(partition.mountpoint)
    dict_parts[partition.device] = [partition.mountpoint, partition.fstype, convert_bytes(partition_usage.total), convert_bytes(partition_usage.used), convert_bytes(partition_usage.free), convert_bytes(partition_usage.percent)]
    # {partiton name: [mountpoint, type, total memory, used memory, free memory, percentage used]}
