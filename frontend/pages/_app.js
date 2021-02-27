import Head from 'next/head'

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
