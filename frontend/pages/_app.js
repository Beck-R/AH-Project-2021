import Head from 'next/head'
import 'antd/dist/antd.min.css';

function MyApp({ Component, pageProps }) {
  return (
    <>
      <Head>
        <title>Remote Monitoring</title>
      </Head>

        <Component {...pageProps} />
    </>)
}

export default MyApp
