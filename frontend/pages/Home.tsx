import Head from "next/head"
import useSWR from "swr"
import {GetServerSideProps} from "next"

import {IComputer} from "../interfaces/IComputer"

import mockComputers from "../mock_data/Computer"
import {ICompCard, CompCard} from "../components/CompCard"
import {IMenuProps, Menu} from "../components/Menu"

import {DefaultPage} from "../components/DefaultPage"

import {useRef} from "react"

import "isomorphic-unfetch"

interface IHomeProps {
    computers: IComputer[]
}

export default function Home(props: IHomeProps) {
    const {computers} = props

    return (
        // include stats of how many computers are active, average memory usage, average cpu usage on top
        <DefaultPage>
            {computers.map((machine) => (
                <CompCard key={machine.machine} computer={machine} />
            ))}
        </DefaultPage>
    )
}

const fetcher = (url: string) => fetch(url).then((r) => r.json())

export const getServerSideProps: GetServerSideProps = async (context) => {
    // const computers: any = await fetcher("https://jasonaa.me/some/url/for/all/machines")

    // this is for development until i have the backend running
    const computers: IComputer[] = mockComputers
    return {props: {computers}}
}
