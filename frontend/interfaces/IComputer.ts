export interface IComputer {

    "os": string,
    "os_release": string,
    "os_version": string,
    "sys_name": string,
    "machine": string,
  
    "cpu": [
      {
        "processor": string,
        "phys_cores": Number,
        "total_cores": Number,
        "min_freq": Number,
        "max_freq": Number,
        "cur_freq": Number,
        "cpu_usage": Number
      }
    ],
  
    "memory": [
      {
        "total_mem": Number,
        "avail_mem": Number,
        "mem_usage": Number,
        "percent_mem": Number
      }
    ],
  
    "disk": [
      {
        "device": string,
        "mountpoint": string,
        "fstype": string,
        "total_size": Number,
        "disk_usage": Number,
        "disk_free": Number,
        "disk_percent": Number,
        "total_read": Number,
        "total_write": Number
  
      }
    ]
  }