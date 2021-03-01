import {DefaultPage} from "../../components/DefaultPage"
import {GetServerSideProps} from "next"
import { useRouter } from 'next/router'
import {Collapse} from 'antd'
const { Panel } = Collapse;
export default function Machine(props) {
    const {computers} = props
    const router = useRouter()
    const { machine } = router.query
    console.log(machine)
    var computer = computers[0]
    for (var m in computers) {
        m = computers[m]
        if (m.init.sys_name == machine) {
            computer = m
        }
    }
    return (
        <DefaultPage title="Machine Info">
            <h1>{computer.init.sys_name}</h1>
            
            <Collapse>
                <Panel header="Raw API Response" key="1">
                    <code>{JSON.stringify(computer)}</code>
                </Panel>
            </Collapse>
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
        //avgProcUsage += computers[machine].computer.cpu.cpu_usage
        //avgMemUsage += parseInt(
        //    computers[machine].computer.memory.percent_mem.split("%")[0]
        //)
    }

    avgProcUsage /= machines.length
    avgMemUsage /= machines.length

    console.dir("********", computers)
    return {
        props: {
            computers: machines,
            //procUsage: avgProcUsage,
            //memUsage: avgMemUsage
        }
    }
}
