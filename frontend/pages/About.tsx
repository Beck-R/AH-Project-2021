import {DefaultPage} from "../components/DefaultPage"

export default function About() {
    return (
        // include stats of how many computers are active, average memory usage, average cpu usage on top
        <DefaultPage title="About">
            <p>See our <a href="https://devpost.com/software/oat-open-access-tool">DevPost submission</a> for a full writeup! <a href="https://github.com/Beck-R/AH-Project-2021">GitHub repo also available.</a></p>
        </DefaultPage>
    )
}