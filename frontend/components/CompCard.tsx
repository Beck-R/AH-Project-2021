import { IComputer } from '../interfaces/IComputer'
import { Card } from 'antd';
import Link from 'next/link'
export interface ICompCard {
    computer: IComputer
    key: string
}

// make this render a card with name, current processor freq and memory usage
// for now it'll just show the machine name
export function CompCard(props: ICompCard) {
    const { computer } = props
    return (
        <Card style={{ width: 300 }} title={computer.init.sys_name} extra={<Link href={"/machines/"+computer.init.sys_name}>More</Link>}>
        <p><b>System Vitals</b></p>
        <p>OS: {computer.init.os} {computer.init.os_release}</p>
        
        <p>Memory: {round(computer.computer.memory.avail_mem)} available out of {round(computer.init.memory.total_mem)} ({computer.computer.memory.percent_mem} used)</p>
        <p>Processor: {round(computer.computer.cpu.cur_freq)} out of {round(computer.init.cpu.max_freq)} ({computer.computer.cpu.cpu_usage}%)</p>
        </Card>
    )
}

function round(num) {
    const thing = num.split(" ")
    return Math.round( thing[0] * 100 + Number.EPSILON ) / 100 + " " + thing[1]
}