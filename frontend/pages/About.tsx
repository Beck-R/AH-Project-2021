import {DefaultPage} from "../components/DefaultPage"

export function About() {
    return (
        // include stats of how many computers are active, average memory usage, average cpu usage on top
        <DefaultPage title="About">
            {/* <CustomRow>
                <Statistic title="Active Computers" value={computers.length} />
                <PercentStat label="Average Memory Usage" stat={memUsage} />
                <PercentStat label="Average Processor Usage" stat={procUsage} />
            </CustomRow>
            <CustomRow>
                {computers.map((machine) => (
                    <CompCard key={machine.init.sys_name} computer={machine} />
                ))}
            </CustomRow> */}
        </DefaultPage>
    )
}