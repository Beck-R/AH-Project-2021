import {IMenuProps, SideMenu} from "./SideMenu"
import {Row, Col} from "antd"

const menuWidth = 4
const contentWidth = 24 - menuWidth

export function DefaultPage(props: any): JSX.Element {
    const {title}=props
    return (
        <Row>
            <Col span={menuWidth}>
                <SideMenu />
            </Col>
            <Col span={contentWidth}>
                <div style={{margin: "none", padding: "2em"}}>
                    <h1>{title}</h1>
                    {props && props.children ? props.children : <></>}
                </div>
            </Col>
        </Row>
    )
}
