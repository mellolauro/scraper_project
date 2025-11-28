import dynamic from 'next/dynamic'
import Head from 'next/head'


const SearchForm = dynamic(() => import('../components/SearchForm'), { ssr: false })


export default function Home() {
    return (
    <>
        <Head>
            <title>Scraper Adherence Dashboard</title>
        </Head>
        <main style={{ padding: 20 }}>
            <SearchForm />
        </main>
    </>
)
}