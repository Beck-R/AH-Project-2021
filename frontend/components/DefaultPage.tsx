import { IMenuProps, SideMenu } from './SideMenu'
import {Row, Col} from 'antd'


export function DefaultPage(props: any) {
    return (
        <Row>
            <Col span="4">
            <SideMenu />
            </Col>
            <Col span="20">
            {props && props.children ? props.children : <></>}
            </Col>
        </Row>
    )
}