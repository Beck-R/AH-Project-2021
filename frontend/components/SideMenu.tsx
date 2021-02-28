import {Menu,Typography} from "antd"
import {
    AppstoreOutlined,
    MenuUnfoldOutlined,
    MenuFoldOutlined,
    PieChartOutlined,
    DesktopOutlined,
    ContainerOutlined,
    MailOutlined,
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
                    backgroundColor: "#1d39c4",
                    display: "flex",
                    justifyContent: "center",
                    alignItems: "center",
                    flexDirection:"column",
                    height: "8vh",
                    padding:"none",
                    color:"whitesmoke"
                    
                }}>
                <RadarChartOutlined style={{fontSize: "2em"}}/>
                <Text type="secondary">Remotus</Text> 
            </div>
            <Menu theme="dark" style={{position: "sticky", height: "100vh"}}>
                <Menu.Item key="1" icon={<ContainerOutlined />}>
                    Home
                </Menu.Item>
            </Menu>
        </>
    )
}
