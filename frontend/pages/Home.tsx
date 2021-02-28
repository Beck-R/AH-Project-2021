import useSWR from "swr"
import {GetServerSideProps} from "next"

import {IComputer} from "../interfaces/IComputer"

import {ICompCard, CompCard} from "../components/CompCard"

import {DefaultPage} from "../components/DefaultPage"

// import "isomorphic-unfetch"

interface IHomeProps {
    computers: IComputer[]
}

export default function Home(props: IHomeProps) {
    const {computers} = props
    console.log(props)

    return (
        // include stats of how many computers are active, average memory usage, average cpu usage on top
        <DefaultPage>
            {computers.map((machine) => (
                <CompCard key={machine.init.sys_name} computer={machine} />
            ))}
        </DefaultPage>
    )
}

const fetcher = (url: string) => fetch(url).then((r) => r.json())

export const getServerSideProps: GetServerSideProps = async (context) => {
    const computers: any = await fetcher(`http://localhost:3000/api/computers/all/sendData`)
    console.log(typeof(computers))
    var machines = []

    for (const machine in computers) {
        machines.push(computers[machine])
    }

    console.log("********", computers)
    return {
        props: {
            computers: machines
        }
    }
}
