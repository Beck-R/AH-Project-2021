
import {Liquid} from "@ant-design/charts"
import {Statistic} from "antd"

export function PercentStat(props: IPercentStat) {
    const {stat, label} = props
    const config = {
        title: {
            formatter: function formatter() {
                return label
            }
        }
    }
    return (
        <div
            style={{
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                justifyContent: "center",
                width: "25%",
                // height: "20vh"
            }}>
            {/* <Liquid statistic={config} percent={stat} renderer="svg"/> */}
            <Statistic title={label} value={stat*100+"%"}/>
        </div>
    )
}

interface IPercentStat {
    stat: number
    label: string
}
