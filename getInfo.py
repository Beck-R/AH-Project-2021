import platform
import psutil
import requests
import json

#Send data to flask server using requests module
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
total_cores = psutil.cpu_count(logical=True)

frequency = psutil.cpu_freq()
min_freq = frequency.min
max_freq = frequency.max
cur_freq = frequency.current

cpu_usage = psutil.cpu_percent()

#memory usage

memory = psutil.virtual_memory()

mem_total = convert_bytes(memory.total)
mem_avail = convert_bytes(memory.available)
mem_usage = convert_bytes(memory.used)
mem_percent = (str(memory.percent) + '%')


#disk Information

parts = psutil.disk_partitions()

for partition in parts:
    device = partition.device
    mp = partition.mountpoint
    fstype = partition.fstype

    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        continue
    
    total_size = convert_bytes(partition_usage.total)
    disk_usage = convert_bytes(partition_usage.used)
    disk_free = convert_bytes(partition_usage.free)
    disk_percent = partition_usage.percent

    # get total read & writes since last boot
    disk_io = psutil.disk_io_counters()
    
    read = convert_bytes(disk_io.read_bytes)
    write = convert_bytes(disk_io.write_bytes)




send_data = {
    "computer" : [
        {
            "os" : operating_system,
            "os_release" : release,
            "os_version" : version,
            "sys_name" : node,
            "machine" : machine,

            "cpu" : [
                {
                    "processor" : processor,
                    "phys_cores" : phys_cores,
                    "total_cores" : total_cores,
                    "min_freq" : min_freq,
                    "max_freq" : max_freq,
                    "cur_freq" : cur_freq,
                    "cpu_usage" : cpu_usage
                }
            ],

            "memory" : [
                {
                    "total_mem" : mem_total,
                    "avail_mem" : mem_avail,
                    "mem_usage" : mem_usage,
                    "percent_mem" : mem_percent
                }
            ],

            "disk" : [
                {
                    "device" : device,
                    "mountpoint" : mp,
                    "fstype" : fstype,
                    "total_size" : total_size,
                    "disk_usage" : disk_usage,
                    "disk_free" : disk_free,
                    "disk_percent" : disk_percent,
                    "total_read" : read,
                    "total_write" : write

                }
            ]
        }
    ]
}

requests.post(f"http://ip.address:port/api/computers/{node}/getData", json = json.dumps(send_data))
