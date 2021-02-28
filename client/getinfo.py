import time
import platform
import psutil
import GPUtil
import requests
import json

# Send data to flask server using requests module
def convert_bytes(bytes):
    factor = 1024
    listValues = ["B", "KB", "MB", "GB", "TB", "PB"]
    for unit in listValues:
        if bytes < factor:
            return (str(bytes) + ' ' + unit)
        bytes = bytes/factor

def scale_freq(freq):
    factor = 1000
    listValues = ["Mhz", "Ghz", "Thz"]
    for unit in listValues:
        if freq < factor:
            return(str(freq) + ' ' + unit)
        freq = freq/factor


def sys_monitor():
    # System Information

    system = platform.uname()

    operating_system = system.system
    node = system.node
    release = system.release
    version = system.version
    machine = system.machine
    processor = system.processor

    # CPU Information

    phys_cores = psutil.cpu_count(logical=False)
    total_cores = psutil.cpu_count(logical=True)

    frequency = psutil.cpu_freq()
    min_freq = scale_freq(frequency.min)
    max_freq = scale_freq(frequency.max)

    cpu_usage = psutil.cpu_percent()

    # memory usage

    memory = psutil.virtual_memory()

    mem_total = convert_bytes(memory.total)


    # onetime data
    start_data = {
        "version": "start",
        "computer" : 
            {
                "os" : operating_system,
                "os_release" : release,
                "os_version" : version,
                "sys_name" : node,
                "machine" : machine,

                "cpu" : 
                    {
                        "processor" : processor,
                        "phys_cores" : phys_cores,
                        "total_cores" : total_cores,
                        "min_freq" : min_freq,
                        "max_freq" : max_freq,
                    },

                "memory" : 
                    {
                        "total_mem" : mem_total,
                    }
            }
        
    }
    base_url = "http://localhost:8080"
    data_url = f"{base_url}/api/computers/{node}/getData"

    requests.post(data_url, json = json.dumps(start_data))

    # realtime data
    while True:
        # realtime cpu
        frequency = psutil.cpu_freq()
        cur_freq = scale_freq(frequency.current)
        cpu_usage = psutil.cpu_percent()
        
        # realtime memory
        mem_avail = convert_bytes(memory.available)
        mem_usage = convert_bytes(memory.used)
        mem_percent = (str(memory.percent) + '%')
        
        # realtime disk
        parts = psutil.disk_partitions()

        list_disks = []
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
        
            disk_io = psutil.disk_io_counters()
            read = convert_bytes(disk_io.read_bytes)
            write = convert_bytes(disk_io.write_bytes)

            list_disks.append({
                "device":device, "mp":mp, "fstype": fstype, "total_size": total_size,
                "disk_usage": disk_usage, "disk_free": disk_free, "disk_percent": disk_percent,
                "read": read, "write": write
            })


        disk_data = {"version": "disks", "disks": list_disks}

        # realtime gpu
        gpus = GPUtil.getGPUs()
        
        list_gpu = []
        for gpu in gpus:
            gpu_id = gpu.id
            gpu_name = gpu.name
            gpu_load = gpu.load*100
            gpu_free_mem = convert_bytes(gpu.memoryFree)
            gpu_used_mem = convert_bytes(gpu.memoryUsed)
            gpu_total_mem = convert_bytes(gpu.memoryTotal)
            gpu_temp = "f{gpu.temperature}℃"
            gpu_uuid = gpu.uuid

            list_gpu.append({
                "gpu_id": gpu_id, "gpu_name": gpu_name, "gpu_load": gpu_load,
                "gpu_free_mem": gpu_free_mem, "gpu_used_mem": gpu_used_mem, "gpu_total_mem": gpu_total_mem,
                "gpu_temp": gpu_temp, "gpu_uuid": gpu_uuid
            })

        gpu_data = {"version": "gpu", "gpus": list_gpu}
        
        # realtime json
        realtime_data = {
            "version": "realtime",
                    "computer" : 
                {
                    "cpu" : 
                        {
                            "cur_freq" : cur_freq,
                            "cpu_usage" : cpu_usage
                        },

                    "memory" : 
                        {
                            "avail_mem" : mem_avail,
                            "mem_usage" : mem_usage,
                            "percent_mem" : mem_percent
                        }
                    
                }
            
        }

        requests.post(data_url, json = json.dumps(realtime_data))
        requests.post(data_url, json = json.dumps(disk_data))
        requests.post(data_url, json = json.dumps(gpu_data))
        time.sleep(5)
