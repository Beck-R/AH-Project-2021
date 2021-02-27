import Head from 'next/head'
import useSWR from 'swr'
import { GetServerSideProps } from 'next'

import 'isomorphic-unfetch';

interface IProps {
  computers: IComputer[],
}

interface IComputer {

  "os": String,
  "os_release": String,
  "os_version": String,
  "sys_name": String,
  "machine": String,

  "cpu": [
    {
      "processor": String,
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
      "device": String,
      "mountpoint": String,
      "fstype": String,
      "total_size": Number,
      "disk_usage": Number,
      "disk_free": Number,
      "disk_percent": Number,
      "total_read": Number,
      "total_write": Number

    }
  ]
}


export default function Home(props: IProps) {
  const { computers } = props
  return (
    <div>

    </div>
  )
}

const fetcher = (url: string) => fetch(url).then(r => r.json())

export const getServerSideProps: GetServerSideProps = async (context) => {
  const computers: any = fetcher("/some/url/for/all/machines")
  return { props: { computers } }
}