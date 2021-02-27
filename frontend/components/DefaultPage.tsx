import { IMenuProps, Menu } from '../components/Menu'


export function DefaultPage(props: any) {
    return (
        <div>
            <Menu />
            {props && props.children ? props.children : <></>}
        </div>
    )
}