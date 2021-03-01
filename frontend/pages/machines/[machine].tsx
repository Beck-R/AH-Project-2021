import {DefaultPage} from "../../components/DefaultPage"
import {GetServerSideProps} from "next"
import { useRouter } from 'next/router'

export default function Machine(props) {
    const {computers} = props
    const router = useRouter()
    const { machineName } = router.query
    const computer = computers[machineName[0]] || ""
    return (
        <DefaultPage title="Machine Info">
            <h1>{computer.init.machine}</h1>
            
            <h6>Raw API Response</h6>
            <code>{JSON.stringify(computer)}</code>
        </DefaultPage>
    )
}

const fetcher = (url: string) => fetch(url).then((r) => r.json())

export const getServerSideProps: GetServerSideProps = async (context) => {
    const computers: any = await fetcher(
        `http://localhost:8080/api/computers/all/sendData`
    ) || {}
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

    avgProcUsage /= machines.length
    avgMemUsage /= machines.length

    console.dir("********", computers)
    return {
        props: {
            computers: machines,
            procUsage: avgProcUsage,
            memUsage: avgMemUsage
        }
    }
}