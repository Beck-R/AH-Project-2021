import {Menu, Typography} from "antd"
import {useRouter} from 'next/router'
import Link from "next/link"
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

const {Title, Text} = Typography

export interface IMenuProps {}

export function SideMenu(props: IMenuProps): JSX.Element {
    const router = useRouter()
    return (
        <>
            <div
                style={{
                    width: "100%",
                    backgroundColor: "#001529",
                    display: "flex",
                    justifyContent: "center",
                    alignItems: "center",
                    flexDirection: "column",
                    height: "8vh",
                    padding: "none",
                    color: "whitesmoke"
                }}>
                <RadarChartOutlined style={{fontSize: "2em"}} />
            </div>
            <Menu defaultSelectedKeys={router.pathname} onClick={(object: Nav) => {router.push(object.key)}} theme="dark" style={{position: "sticky", height: "100vh"}}>
                <Menu.Item key="/Home" icon={<ContainerOutlined />}>
                    Home
                </Menu.Item>
                <Menu.Item key="/About" icon={<QuestionOutlined />}>
                    About
                </Menu.Item>
            </Menu>
        </>
    )
}

interface Nav {
    item: string
    key: string
    keyPath: string
    domEvent: any
}

