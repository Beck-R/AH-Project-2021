import { IComputer } from '../interfaces/IComputer'
import { Card } from 'antd';

export interface ICompCard {
    computer: IComputer
    key: string
}

// make this render a card with name, current processor freq and memory usage
// for now it'll just show the machine name
export function CompCard(props: ICompCard) {
    const { computer } = props
    return (
        <Card style={{ width: 300 }} title={computer.init.sys_name} extra={<a href={"/machines/"+computer.init.sys_name}>More</a>}>
        <p><b>System Vitals</b></p>
        <p>OS: {computer.init.os} {computer.init.os_release}</p>
        <p>Memory: {computer.computer.memory.avail_mem} available out of {computer.init.memory.total_mem} ({computer.computer.memory.percent_mem} used)</p>
        <p>Processor: {computer.computer.cpu.cur_freq} out of {computer.init.cpu.max_freq} ({computer.computer.cpu.cpu_usage}%)</p>
        </Card>
    )
}