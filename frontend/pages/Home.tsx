import useSWR from "swr"
import {GetServerSideProps} from "next"

import {IComputer} from "../interfaces/IComputer"

import {ICompCard, CompCard} from "../components/CompCard"

import {PercentStat} from "../components/PercentStat"

import {DefaultPage} from "../components/DefaultPage"

import {Statistic} from "antd"

interface IHomeProps {
    computers: IComputer[]
    memUsage: number
    procUsage: number
}

function CustomRow(props) {
    return (
        <div
            style={{
                display: "flex",
                alignItems: "center",
                margin: "1em",
                padding: "1em"
            }}>
            {props && props.children ? props.children : <></>}
        </div>
    )
}

export default function Home(props: IHomeProps) {
    const {computers, memUsage, procUsage} = props
    console.log(props)

    return (
        // include stats of how many computers are active, average memory usage, average cpu usage on top
        <DefaultPage title="Home">
            <CustomRow>
                <Statistic title="Active Computers" value={computers.length} />
                <PercentStat label="Average Memory Usage" stat={memUsage} />
                <PercentStat label="Average Processor Usage" stat={procUsage} />
            </CustomRow>
            <CustomRow>
                {computers.map((machine) => (
                    <CompCard key={machine.init.sys_name} computer={machine} />
                ))}
            </CustomRow>
        </DefaultPage>
    )
}

const fetcher = (url: string) => fetch(url).then((r) => r.json())

export const getServerSideProps: GetServerSideProps = async (context) => {
    const computers: any = await fetcher(
        `http://localhost:8080/api/computers/all/sendData`
    )
    console.log(typeof computers)
    var machines = []
    var avgProcUsage = 0
    var avgMemUsage = 0
    for (const machine in computers) {
        machines.push(computers[machine])
        console.dir(computers[machine])
        avgProcUsage += computers[machine].computer.cpu.cpu_usage
        avgMemUsage += parseInt(
            computers[machine].computer.memory.percent_mem.split("%")[0]
        )
    }

    avgProcUsage /= 100 / machines.length
    avgMemUsage /= 100 / machines.length

    console.dir("********", computers)
    return {
        props: {
            computers: machines,
            procUsage: avgProcUsage,
            memUsage: avgMemUsage
        }
    }
}
