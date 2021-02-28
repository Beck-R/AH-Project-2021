import {IMenuProps, SideMenu} from "./SideMenu"
import {Row, Col} from "antd"

const menuWidth = 4
const contentWidth = 24 - menuWidth

export function DefaultPage(props: any): JSX.Element {
    return (
        <Row>
            <Col span={menuWidth}>
                <SideMenu />
            </Col>
            <Col span={contentWidth}>
                <div style={{margin: "none", padding: "1em"}}>
                    {props && props.children ? props.children : <></>}
                </div>
            </Col>
        </Row>
    )
}
