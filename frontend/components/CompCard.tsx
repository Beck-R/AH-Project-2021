import { IComputer } from '../interfaces/IComputer'

export interface ICompCard {
    computer: IComputer
    key: string
}

// make this render a card with name, current processor freq and memory usage
// for now it'll just show the machine name
export function CompCard(props: ICompCard) {
    const { computer } = props
    return (
        <p>{computer.sys_name}</p>
    )
}