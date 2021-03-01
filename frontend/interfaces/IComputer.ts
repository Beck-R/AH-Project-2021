export interface IComputer {
    init: {
        os: string
        os_release: string
        os_version: string
        sys_name: string
        machine: string
        cpu: {
            processor: string
            phys_cores: string
            total_cores: string
            min_freq: string
            max_freq: string
        }
        memory: {
            total_mem: string
        }
    }

    disks: [
        {
            device: string
            mp: string
            fstype: string
            total_size: number
            disk_usage: number
            disk_free: number
            disk_percent: number
            read: number
            write: number
        }
    ]

    gpus?: [
        {
            gpu_id: number
            gpu_name: string
            gpu_load: number
            gpu_free_mem: string
            gpu_used_mem: string
            gpu_total_mem: string
            gpu_temp: string
            gpu_uuid: string
        }
    ]

    computer: {
        cpu: {
            cur_freq: string
            cpu_usage: number
        }
        memory: {
            avail_mem: string
            mem_usage: string
            percent_mem: string
        }
    }
}
