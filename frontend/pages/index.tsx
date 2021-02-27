import Head from 'next/head'

interface theProps {
  computers: Computer[],
}

interface Computer {
  
    "os" : String,
    "os_release" : String,
    "os_version" : String,
    "sys_name" : String,
    "machine" : String,

    "cpu" : [
        {
            "processor" : String,
            "phys_cores" : Number,
            "total_cores" : Number,
            "min_freq" : Number,
            "max_freq" : Number,
            "cur_freq" : Number,
            "cpu_usage" : Number
        }
    ],

    "memory" : [
        {
            "total_mem" : Number,
            "avail_mem" : Number,
            "mem_usage" : Number,
            "percent_mem" : Number
        }
    ],

    "disk" : [
        {
            "device" : String,
            "mountpoint" : String,
            "fstype" : String,
            "total_size" : Number,
            "disk_usage" : Number,
            "disk_free" : Number,
            "disk_percent" : Number,
            "total_read" : Number,
            "total_write" : Number

        }
    ]
}


export default function Home(props: theProps) {
  const {computers} = props
  return (
    <div>
      
    </div>
  )
}
