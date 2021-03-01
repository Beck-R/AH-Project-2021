import {Menu,Typography} from "antd"
import Link from 'next/link'
import {
    AppstoreOutlined,
    MenuUnfoldOutlined,
    MenuFoldOutlined,
    PieChartOutlined,
    DesktopOutlined,
    ContainerOutlined,
    MailOutlined,
    QuestionOutlined,
    RadarChartOutlined
} from "@ant-design/icons"

const {Title, Text } = Typography

export interface IMenuProps {}

export function SideMenu(props: IMenuProps): JSX.Element {
    return (
        <>
            <div
                style={{
                    width: "100%",
                    backgroundColor: "#001529",
                    display: "flex",
                    justifyContent: "center",
                    alignItems: "center",
                    flexDirection:"column",
                    height: "8vh",
                    padding:"none",
                    color:"whitesmoke"
                    
                }}>
                <RadarChartOutlined style={{fontSize: "2em"}}/>
            </div>
            <Menu theme="dark" style={{position: "sticky", height: "100vh"}}>
                <Link href="/Home"><Menu.Item key="1" icon={<ContainerOutlined />}>
                    Home
                </Menu.Item></Link>
                <Link href="/About"><Menu.Item key="1" icon={<QuestionOutlined />}>
                    About
                </Menu.Item></Link>
            </Menu>
        </>
    )
}
